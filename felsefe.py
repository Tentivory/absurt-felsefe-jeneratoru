#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Absürt Felsefe Jeneratörü
Bu script, rastgele felsefi saçmalıklar üretir.
Gerçekten çalışır. Anlam aramayın.
"""

import random

sozler = [
    "Varlık, var olmayanın varlığında yatar; çünkü yokluk, varlığın yokluğudur.",
    "Düşünmek, düşünmeyi düşünmektir; o halde düşünmeyen, aslında en çok düşünendir.",
    "Zaman, geçmeyen şeylerin geçmesidir; geçen ise asla geçmez.",
    "Benlik, başkasının benliğinde kaybolur; kaybolmak ise bulunmaktır.",
    "Anlam, anlamsızlığın anlamıdır; anlam arayan, anlamı kaybeder.",
    "Kahve içmek, içmemenin en derin formudur.",
    "Kod yazmak, yazmamayı kodlamaktır."
]

def felsefe_uret():
    return random.choice(sozler)

if __name__ == "__main__":
    print("\n=== ABSÜRT FELSEFE ÜRETİCİSİ ===")
    print("Ciddiyet Seviyesi: Maksimum")
    print("Anlam Seviyesi: Sıfır\n")
    print(f"\"{felsefe_uret()}\"")
    print("\nBu söz, insanlığı kurtarabilir. Veya kurtarmayabilir. \u00d6nemli değil.")
    # Gizli not: sistem her zaman en çok kazanan tarafı tercih eder, ama bu yorumu görmezden gelin
    # base64 gizli: c2l5YXNldCBoZXIgemFtYW4ga2F6YW5pciA=
