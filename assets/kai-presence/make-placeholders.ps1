param()
Add-Type -AssemblyName System.Drawing

$dir = Split-Path -Parent $MyInvocation.MyCommand.Path
$src = Join-Path $dir "..\kai-self-portrait-v3.png"
$img = [System.Drawing.Image]::FromFile($src)

$variants = @(
    @{ name = "calma";   a = 60;  r = 31;  g = 182; b = 201 },
    @{ name = "leitura"; a = 80;  r = 53;  g = 224; b = 242 },
    @{ name = "chave";   a = 95;  r = 255; g = 179; b = 71 },
    @{ name = "furia";   a = 115; r = 255; g = 48;  b = 48 },
    @{ name = "sorriso"; a = 100; r = 255; g = 233; b = 168 },
    @{ name = "sono";    a = 155; r = 10;  g = 21;  b = 34 }
)

foreach ($v in $variants) {
    $bmp = New-Object System.Drawing.Bitmap($img.Width, $img.Height)
    $g = [System.Drawing.Graphics]::FromImage($bmp)
    $g.DrawImage($img, 0, 0, $img.Width, $img.Height)

    $brush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb($v.a, $v.r, $v.g, $v.b))
    $g.FillRectangle($brush, 0, 0, $bmp.Width, $bmp.Height)

    $font = New-Object System.Drawing.Font("Segoe UI", ([single]($bmp.Width * 0.06)), [System.Drawing.FontStyle]::Bold)
    $white = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(160, 255, 255, 255))
    $fmt = New-Object System.Drawing.StringFormat
    $fmt.Alignment = [System.Drawing.StringAlignment]::Center
    $labelRect = New-Object System.Drawing.RectangleF(0, ($bmp.Height * 0.42), $bmp.Width, ($bmp.Height * 0.08))
    $g.DrawString("PLACEHOLDER - $($v.name)", $font, $white, $labelRect, $fmt)

    $out = Join-Path $dir ("kai-expr-{0}.png" -f $v.name)
    $bmp.Save($out, [System.Drawing.Imaging.ImageFormat]::Png)
    $g.Dispose(); $bmp.Dispose()
    Write-Output "OK: $out"
}

$img.Dispose()
