// Canon RP kurs — L1-07-V03: rysunek z instrukcji PL, s. 100, krok 2
// (dolny pasek ekranu z „F5.6” i skalą jasności). D-056: plik wynikowy kończy
// się na -canon i zostaje lokalnie (production/assets/, poza Git).
//
// Użycie (z katalogu głównego repozytorium):
//   swift production/l1-07/v03/prepare_v03_canon.swift <pdf> <strona> <skala> <wyjście.png> [x y szer wys]
// Prostokąt wycinka w punktach PDF, początek w lewym górnym rogu strony.
// Bez prostokąta zapisuje całą stronę (do odszukania rysunku).
// Wycinek V03 (22.10.2026):
//   swift production/l1-07/v03/prepare_v03_canon.swift \
//     materials/canon-official/Canon-EOS-RP-Zaawansowana-instrukcja-PL-2019.pdf 100 15 \
//     production/assets/l1-07/l1-07-v03-liczba-f-canon.png 16.9 254.2 91 11.5
import AppKit
import PDFKit

let a = CommandLine.arguments
guard a.count == 5 || a.count == 9,
      let doc = PDFDocument(url: URL(fileURLWithPath: a[1])),
      let pageNo = Int(a[2]), let scale = Double(a[3]),
      let page = doc.page(at: pageNo - 1) else {
    FileHandle.standardError.write("argumenty: pdf strona skala wyjście [x y szer wys]\n".data(using: .utf8)!)
    exit(1)
}
let box = page.bounds(for: .mediaBox)
var rect = CGRect(x: 0, y: 0, width: box.width, height: box.height)
if a.count == 9, let x = Double(a[5]), let y = Double(a[6]), let w = Double(a[7]), let h = Double(a[8]) {
    rect = CGRect(x: x, y: y, width: w, height: h)
}
let pw = Int((rect.width * scale).rounded()), ph = Int((rect.height * scale).rounded())
let cs = CGColorSpace(name: CGColorSpace.sRGB)!
let ctx = CGContext(data: nil, width: pw, height: ph, bitsPerComponent: 8, bytesPerRow: 0,
                    space: cs, bitmapInfo: CGImageAlphaInfo.premultipliedLast.rawValue)!
ctx.setFillColor(CGColor(red: 1, green: 1, blue: 1, alpha: 1))
ctx.fill(CGRect(x: 0, y: 0, width: pw, height: ph))
ctx.scaleBy(x: scale, y: scale)
// przesunięcie: wycinek liczony od góry strony, PDF od dołu
ctx.translateBy(x: -rect.minX - box.minX, y: -(box.height - rect.maxY) - box.minY)
page.draw(with: .mediaBox, to: ctx)
let img = ctx.makeImage()!
let rep = NSBitmapImageRep(cgImage: img)
try! rep.representation(using: .png, properties: [:])!.write(to: URL(fileURLWithPath: a[4]))
print("ZAPISANO \(a[4]) \(pw)x\(ph) px; strona \(pageNo) \(Int(box.width))x\(Int(box.height)) pt")
