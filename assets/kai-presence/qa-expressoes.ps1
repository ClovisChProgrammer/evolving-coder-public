Add-Type -AssemblyName System.Drawing
$dir = Split-Path -Parent $MyInvocation.MyCommand.Path

$expected = @{
    "calma"   = @{ r = 31;  g = 182; b = 201; desc = "ciano-oceano" }
    "leitura" = @{ r = 53;  g = 224; b = 242; desc = "ciano eletrico" }
    "chave"   = @{ r = 255; g = 179; b = 71;  desc = "ambar forja" }
    "furia"   = @{ r = 255; g = 48;  b = 48;  desc = "vermelho alarme" }
    "sorriso" = @{ r = 255; g = 233; b = 168; desc = "dourado champanhe" }
    "sono"    = @{ r = 10;  g = 21;  b = 34;  desc = "azul-meia-noite" }
}

foreach ($name in $expected.Keys) {
    $path = Join-Path $dir ("kai-expr-{0}.png" -f $name)
    if (-not (Test-Path $path)) { Write-Output "[$name] FALTANDO"; continue }

    $img = [System.Drawing.Bitmap]::FromFile($path)
    $w = $img.Width; $h = $img.Height
    $prop = [math]::Round($w / $h, 3)

    $cx = [int]($w * 0.5); $cy = [int]($h * 0.35)
    $rw = [int]($w * 0.5); $rh = [int]($h * 0.45)
    $sumR = 0L; $sumG = 0L; $sumB = 0L; $n = 0
    for ($x = $cx - [int]($rw/2); $x -lt $cx + [int]($rw/2); $x += 8) {
        for ($y = $cy - [int]($rh/2); $y -lt $cy + [int]($rh/2); $y += 8) {
            if ($x -lt 0 -or $y -lt 0 -or $x -ge $w -or $y -ge $h) { continue }
            $c = $img.GetPixel($x, $y)
            $sumR += $c.R; $sumG += $c.G; $sumB += $c.B; $n++
        }
    }
    $avgR = [math]::Round($sumR / $n); $avgG = [math]::Round($sumG / $n); $avgB = [math]::Round($sumB / $n)

    $e = $expected[$name]
    $dist = [math]::Sqrt([math]::Pow($avgR - $e.r, 2) + [math]::Pow($avgG - $e.g, 2) + [math]::Pow($avgB - $e.b, 2))

    Write-Output ("[{0}] {1}x{2} prop={3} | media centro RGB=({4},{5},{6}) | esperado {7} ({8},{9},{10}) | dist={11}" -f `
        $name, $w, $h, $prop, $avgR, $avgG, $avgB, $e.desc, $e.r, $e.g, $e.b, [math]::Round($dist))

    $img.Dispose()
}
