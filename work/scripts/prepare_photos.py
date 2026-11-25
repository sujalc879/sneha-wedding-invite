#!/usr/bin/env python3
"""Prepare supplied originals without modifying them; inspect every crop visually."""
from pathlib import Path
import argparse
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[2]


def save_clean(image, target):
    oriented = ImageOps.exif_transpose(image).convert('RGB')
    oriented.thumbnail((1200, 1200), Image.Resampling.LANCZOS)
    clean = Image.new('RGB', oriented.size)
    clean.paste(oriented)
    quality = 82
    while True:
        clean.save(target, 'JPEG', quality=quality, optimize=True, progressive=True)
        if target.stat().st_size <= 250_000 or quality <= 72:
            break
        quality -= 2
    return clean


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--files', nargs='*', help='Original file names in DETAILS.md order; defaults to sorted originals.')
    args = parser.parse_args()
    originals = ROOT / 'originals'
    paths = [originals / name for name in args.files] if args.files else sorted(p for p in originals.iterdir() if p.is_file() and not p.name.startswith('.'))
    if not paths:
        raise SystemExit('No supplied originals; nothing was generated.')
    if len(paths) > 5:
        raise SystemExit('More than five originals: choose the intended files with --files before processing.')
    public = ROOT / 'public'
    public.mkdir(exist_ok=True)
    for index, source in enumerate(paths, 1):
        if source.resolve().parent != originals.resolve():
            raise SystemExit('Input must be inside originals/.')
        target = public / f'photo{index}.jpg'
        try:
            with Image.open(source) as image:
                clean = save_clean(image, target)
        except Exception as exc:
            raise SystemExit(f'Cannot read {source.name}: export a JPEG first. {exc}')
        with Image.open(target) as check:
            assert not check.getexif() and max(check.size) <= 1200
        print(f'{source.name} -> {target.name}: {clean.width}x{clean.height}, {target.stat().st_size} bytes; crop review required.')
    print('Choose and inspect a face-safe 1200x630 OG crop separately; no automatic OG face crop is made.')


if __name__ == '__main__':
    main()
