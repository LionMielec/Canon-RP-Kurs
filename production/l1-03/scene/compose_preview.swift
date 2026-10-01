// SPDX-License-Identifier: GPL-2.0-or-later
//
// Canon RP kurs — zestawia podglądy obok siebie na jednej planszy z podpisami.
// Plik roboczy produkcji (nie trafia do aplikacji).
//
// Użycie:
//   swift production/l1-03/scene/compose_preview.swift OUT.png "Podpis 1" a.png "Podpis 2" b.png ...

import AppKit

let args = Array(CommandLine.arguments.dropFirst())
guard args.count >= 3, (args.count - 1) % 2 == 0 else {
    fatalError("Użycie: OUT.png PODPIS OBRAZ [PODPIS OBRAZ ...]")
}
let outPath = args[0]
var items: [(String, NSBitmapImageRep)] = []
var i = 1
while i < args.count {
    guard let data = FileManager.default.contents(atPath: args[i + 1]),
          let rep = NSBitmapImageRep(data: data) else { fatalError("Nie można wczytać \(args[i + 1])") }
    items.append((args[i], rep))
    i += 2
}

let gap = 24, margin = 24, labelHeight = 64
let cellW = items.map { $0.1.pixelsWide }.max()!
let cellH = items.map { $0.1.pixelsHigh }.max()!
let width = margin * 2 + cellW * items.count + gap * (items.count - 1)
let height = margin * 2 + cellH + labelHeight

let canvas = NSBitmapImageRep(bitmapDataPlanes: nil, pixelsWide: width, pixelsHigh: height,
                              bitsPerSample: 8, samplesPerPixel: 4, hasAlpha: true, isPlanar: false,
                              colorSpaceName: .deviceRGB, bytesPerRow: 0, bitsPerPixel: 0)!
canvas.size = NSSize(width: width, height: height)
NSGraphicsContext.saveGraphicsState()
NSGraphicsContext.current = NSGraphicsContext(bitmapImageRep: canvas)
NSColor.white.setFill()
NSRect(x: 0, y: 0, width: width, height: height).fill()

let style = NSMutableParagraphStyle()
style.alignment = .center
let attrs: [NSAttributedString.Key: Any] = [
    .font: NSFont.systemFont(ofSize: 34, weight: .semibold),
    .foregroundColor: NSColor(calibratedWhite: 0.15, alpha: 1),
    .paragraphStyle: style,
]
for (n, (label, rep)) in items.enumerated() {
    let x = margin + n * (cellW + gap)
    rep.draw(in: NSRect(x: x, y: margin + labelHeight, width: rep.pixelsWide, height: rep.pixelsHigh))
    (label as NSString).draw(in: NSRect(x: x, y: margin + 8, width: cellW, height: labelHeight - 16),
                             withAttributes: attrs)
}
NSGraphicsContext.restoreGraphicsState()
try! canvas.representation(using: .png, properties: [:])!.write(to: URL(fileURLWithPath: outPath))
print("Zapisano \(outPath) (\(width)×\(height))")
