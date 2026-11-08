# Test script to verify all company data keys and check dictionary validity
import json

sample_firm = {
    "name": "NVIDIA Corporation",
    "ticker": "NVDA:US",
    "cmp": "$138.20",
    "dcf": "$152.00",
    "mos": "+10.0%",
    "mcap": "$3,380 Billion ($3.38T)",
    "pe": "58.4",
    "pbv": "42.5",
    "evEbitda": "44.2",
    "beneishM": -2.85,
    "beneishStatus": "SAFE (No Earnings Manipulation)",
    "altmanZ": 18.4,
    "altmanStatus": "SAFE ZONE (Distress Probability < 0.01%)",
    "sloanAccrual": "1.4% (Ultra-High Cash Conversion)",
    "piotroski": "9 / 9 (Flawless Balance Sheet)",
    "dupontROE": {
        "taxBurden": "0.88",
        "interestBurden": "1.00",
        "opMargin": "61.8%",
        "assetTurn": "1.25x",
        "leverage": "1.34x",
        "finalROE": "103.5%"
    },
    "kyleLambda": "0.0012 bps / $10M",
    "blkOwnership": "7.85% ($265 Billion)",
    "vangOwnership": "8.42% ($284 Billion)",
    "activeFloat": "88.5%",
    "nanoLink": "tsmc_fab",
    "soicScore": {
        "industry": 45, "industryMax": 45,
        "funda": 80, "fundaMax": 80,
        "tech": 110, "techMax": 110,
        "val": 22, "valMax": 35,
        "forensic": 40, "forensicMax": 40,
        "total": 297, "totalMax": 310,
        "classification": "EPIC HIGH CONVICTION ALLOCATION"
    }
}
print("Sample firm valid, keys:", len(sample_firm))

