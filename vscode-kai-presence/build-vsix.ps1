Add-Type -AssemblyName System.IO.Compression.FileSystem

$src = "C:\Users\clovi\.config\opencode\skills\evolving-coder\vscode-kai-presence"
$out = "$src\kai-presence-0.2.0.vsix"
if (Test-Path $out) { Remove-Item $out -Force }

$zip = [System.IO.Compression.ZipFile]::Open($out, "Create")

function add($srcPath, $entryName) {
    $bytes = [IO.File]::ReadAllBytes($srcPath)
    $e = $zip.CreateEntry($entryName, "Optimal")
    $ws = $e.Open()
    $ws.Write($bytes, 0, $bytes.Length)
    $ws.Dispose()
}

$manifest = @"
<?xml version="1.0" encoding="utf-8"?>
<PackageManifest Version="2.0.0" xmlns="http://schemas.microsoft.com/developer/vsx-schema/2011" xmlns:d="http://schemas.microsoft.com/developer/vsx-schema-design/2011">
  <Metadata>
    <Identity Language="en-US" Id="kai-presence" Version="0.2.0" Publisher="kai-local" />
    <DisplayName>KAI Presence</DisplayName>
    <Description xml:space="preserve">Presença viva da KAI dentro do VS Code - retrato reativo ao estado real das sessões opencode.</Description>
    <Tags></Tags>
    <Categories>Other</Categories>
    <GalleryFlags>Public</GalleryFlags>
    <Properties>
      <Property Id="Microsoft.VisualStudio.Code.Engine" Value="^1.80.0" />
      <Property Id="Microsoft.VisualStudio.Code.ExtensionKind" Value="workspace" />
      <Property Id="Microsoft.VisualStudio.Code.ExecutesCode" Value="true" />
    </Properties>
  </Metadata>
  <Installation>
    <InstallationTarget Id="Microsoft.VisualStudio.Code"/>
  </Installation>
  <Dependencies/>
  <Assets>
    <Asset Type="Microsoft.VisualStudio.Code.Manifest" Path="extension/package.json" Addressable="true" />
    <Asset Type="Microsoft.VisualStudio.Services.Content.Details" Path="extension/readme.md" Addressable="true" />
  </Assets>
</PackageManifest>
"@
[IO.File]::WriteAllText("$src\extension.vsixmanifest", $manifest, [Text.Encoding]::UTF8)

$contentTypes = @"
<?xml version="1.0" encoding="utf-8"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension=".js" ContentType="application/javascript"/>
<Default Extension=".json" ContentType="application/json"/>
<Default Extension=".md" ContentType="text/markdown"/>
<Default Extension=".svg" ContentType="image/svg+xml"/>
<Default Extension=".vsixmanifest" ContentType="text/xml"/>
</Types>
"@
[IO.File]::WriteAllText("$src\[Content_Types].xml", $contentTypes, [Text.Encoding]::UTF8)

add "$src\[Content_Types].xml" "[Content_Types].xml"
add "$src\extension.vsixmanifest" "extension.vsixmanifest"
add "$src\package.json" "extension/package.json"
add "$src\extension.js" "extension/extension.js"
add "$src\README.md" "extension/readme.md"
add "$src\media\kai-icon.svg" "extension/media/kai-icon.svg"

$zip.Dispose()
"Built: $out"