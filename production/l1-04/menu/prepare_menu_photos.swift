// Przygotowanie zdjęć ekranu aparatu Ani do L1-04 (V13, V14, V16) — D-081.
//
// Dla każdego zdjęcia z iPhone'a:
//   1. wczytuje oryginał z uwzględnieniem orientacji EXIF,
//   2. znajduje cztery rogi świecącego ekranu aparatu (jasność ponad progiem),
//   3. prostuje perspektywę i kadruje sam ekran (bez czarnego otoczenia),
//   4. zapisuje JPEG w sRGB bez metadanych (bez GPS, D-053).
//
// Uruchomienie z katalogu głównego repozytorium:
//   swift production/l1-04/menu/prepare_menu_photos.swift <wejście> <wyjście> [próg] [podgląd-rogów.jpg]
//
// Oryginały są lokalnie w materials/camera-check-2026-10-11/ (poza Git).

import Foundation
import CoreImage
import ImageIO
import UniformTypeIdentifiers

let outputWidth = 1200
let outputHeight = 800   // ekran EOS RP ma proporcje 3:2

let args = CommandLine.arguments
guard args.count >= 3 else {
    FileHandle.standardError.write("Użycie: prepare_menu_photos.swift <wejście> <wyjście> [próg] [podgląd]\n".data(using: .utf8)!)
    exit(1)
}
let inputURL = URL(fileURLWithPath: args[1])
let outputURL = URL(fileURLWithPath: args[2])
// Próg 0,045: górny pasek menu jest prawie czarny, ale jaśniejszy od otoczenia ekranu.
let threshold: Double = args.count >= 4 ? Double(args[3])! : 0.045
let debugURL: URL? = args.count >= 5 ? URL(fileURLWithPath: args[4]) : nil

let context = CIContext(options: [.workingColorSpace: CGColorSpace(name: CGColorSpace.sRGB)!])

guard let loaded = CIImage(contentsOf: inputURL, options: [.applyOrientationProperty: true]) else {
    FileHandle.standardError.write("Nie można wczytać \(inputURL.path)\n".data(using: .utf8)!)
    exit(1)
}
// Początek układu w (0,0), oś y w górę (konwencja Core Image).
let image = loaded.transformed(by: CGAffineTransform(translationX: -loaded.extent.minX, y: -loaded.extent.minY))
let fullW = image.extent.width
let fullH = image.extent.height

// Wyszukiwanie rogów na pomniejszonej kopii.
let scale = 600.0 / Double(max(fullW, fullH))
let small = image.transformed(by: CGAffineTransform(scaleX: scale, y: scale))
let sw = Int(small.extent.width.rounded(.down))
let sh = Int(small.extent.height.rounded(.down))
var pixels = [UInt8](repeating: 0, count: sw * sh * 4)
context.render(small, toBitmap: &pixels, rowBytes: sw * 4,
               bounds: CGRect(x: 0, y: 0, width: sw, height: sh),
               format: .RGBA8, colorSpace: CGColorSpace(name: CGColorSpace.sRGB)!)

// Maska jasnych pikseli; zostaje największy spójny obszar (ekran), bez odblasków.
var mask = [Bool](repeating: false, count: sw * sh)
for i in 0..<(sw * sh) {
    let r = Double(pixels[i * 4]), g = Double(pixels[i * 4 + 1]), b = Double(pixels[i * 4 + 2])
    mask[i] = (0.2126 * r + 0.7152 * g + 0.0722 * b) / 255.0 > threshold
}
var label = [Int](repeating: 0, count: sw * sh)
var best = (id: 0, size: 0)
var nextId = 0
for start in 0..<(sw * sh) where mask[start] && label[start] == 0 {
    nextId += 1
    var stack = [start]
    label[start] = nextId
    var size = 0
    while let p = stack.popLast() {
        size += 1
        let x = p % sw, y = p / sw
        for (dx, dy) in [(1, 0), (-1, 0), (0, 1), (0, -1)] {
            let nx = x + dx, ny = y + dy
            if nx < 0 || ny < 0 || nx >= sw || ny >= sh { continue }
            let q = ny * sw + nx
            if mask[q] && label[q] == 0 { label[q] = nextId; stack.append(q) }
        }
    }
    if size > best.size { best = (nextId, size) }
}

// Rogi jako punkty skrajne w kierunkach przekątnych (bitmapa: y w dół).
var tl = (x: 0, y: 0, v: Int.max), br = (x: 0, y: 0, v: Int.min)
var tr = (x: 0, y: 0, v: Int.min), bl = (x: 0, y: 0, v: Int.max)
for y in 0..<sh {
    for x in 0..<sw where label[y * sw + x] == best.id {
        if x + y < tl.v { tl = (x, y, x + y) }
        if x + y > br.v { br = (x, y, x + y) }
        if x - y > tr.v { tr = (x, y, x - y) }
        if x - y < bl.v { bl = (x, y, x - y) }
    }
}
// Przeliczenie na pełną rozdzielczość i układ Core Image (y w górę).
func toFull(_ x: Int, _ y: Int) -> CGPoint {
    CGPoint(x: (Double(x) + 0.5) / scale, y: Double(fullH) - (Double(y) + 0.5) / scale)
}
let pTL = toFull(tl.x, tl.y), pTR = toFull(tr.x, tr.y)
let pBL = toFull(bl.x, bl.y), pBR = toFull(br.x, br.y)
print("rogi (px, y od góry): TL \(Int(pTL.x)),\(Int(fullH - pTL.y))  TR \(Int(pTR.x)),\(Int(fullH - pTR.y))  BR \(Int(pBR.x)),\(Int(fullH - pBR.y))  BL \(Int(pBL.x)),\(Int(fullH - pBL.y))")

// Prostowanie perspektywy, skala do rozmiaru docelowego.
let corrected = image.applyingFilter("CIPerspectiveCorrection", parameters: [
    "inputTopLeft": CIVector(cgPoint: pTL),
    "inputTopRight": CIVector(cgPoint: pTR),
    "inputBottomLeft": CIVector(cgPoint: pBL),
    "inputBottomRight": CIVector(cgPoint: pBR),
])
let c = corrected.transformed(by: CGAffineTransform(translationX: -corrected.extent.minX, y: -corrected.extent.minY))
let fitted = c.transformed(by: CGAffineTransform(scaleX: Double(outputWidth) / c.extent.width,
                                                 y: Double(outputHeight) / c.extent.height))
    .cropped(to: CGRect(x: 0, y: 0, width: outputWidth, height: outputHeight))

func writeJPEG(_ img: CIImage, to url: URL) {
    guard let cg = context.createCGImage(img, from: img.extent, format: .RGBA8,
                                         colorSpace: CGColorSpace(name: CGColorSpace.sRGB)!),
          let dest = CGImageDestinationCreateWithURL(url as CFURL, UTType.jpeg.identifier as CFString, 1, nil) else {
        FileHandle.standardError.write("Nie można zapisać \(url.path)\n".data(using: .utf8)!)
        exit(1)
    }
    // Brak słownika metadanych: plik nie zawiera EXIF ani GPS.
    CGImageDestinationAddImage(dest, cg, [kCGImageDestinationLossyCompressionQuality: 0.86] as CFDictionary)
    CGImageDestinationFinalize(dest)
}
writeJPEG(fitted, to: outputURL)
print("zapisano \(outputURL.path) (\(outputWidth)×\(outputHeight))")

// Opcjonalny podgląd: oryginał z zaznaczonymi rogami.
if let debugURL = debugURL {
    var overlay = image
    for p in [pTL, pTR, pBR, pBL] {
        let dot = CIImage(color: CIColor(red: 0, green: 1, blue: 0))
            .cropped(to: CGRect(x: p.x - 25, y: p.y - 25, width: 50, height: 50))
        overlay = dot.composited(over: overlay)
    }
    let preview = overlay.transformed(by: CGAffineTransform(scaleX: 1000 / Double(fullH), y: 1000 / Double(fullH)))
    writeJPEG(preview, to: debugURL)
}
