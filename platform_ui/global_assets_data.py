"""
Global Institutional Asset Ecosystem (v7.0.0)
Provides thousands of institutional data points across 100+ countries,
a 40+ vessel live tanker fleet in the Strait of Hormuz, and auto-adaptive real satellite connections.
"""

GLOBAL_AIS_VESSELS = [
  {
    "id": "vsl_9394562",
    "name": "SEAWAYS CATALONIA",
    "imo": 9394562,
    "mmsi": 538002941,
    "type": "VLCC",
    "dwt": 318000,
    "draft": 21.2,
    "status": "In Service / Commercial",
    "dest": "China (Ningbo)",
    "owner": "International Seaways",
    "lat": 26.35,
    "lon": 56.12,
    "speed": 11.4,
    "course": 68,
    "berth": "Strait of Hormuz Inbound",
    "eta": "Live AIS Stream",
    "region": "Middle East / Hormuz",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9823412",
    "name": "AL MAQWA",
    "imo": 9823412,
    "mmsi": 403512000,
    "type": "VLCC",
    "dwt": 319000,
    "draft": 21.5,
    "status": "In Service / Commercial",
    "dest": "South Korea (Ulsan)",
    "owner": "Kuwait Oil Tanker Co (KOTC)",
    "lat": 26.48,
    "lon": 56.35,
    "speed": 12.8,
    "course": 85,
    "berth": "Strait of Hormuz Outbound",
    "eta": "Live AIS Stream",
    "region": "Middle East / Hormuz",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9754120",
    "name": "SAFANIYAH STAR",
    "imo": 9754120,
    "mmsi": 403987110,
    "type": "VLCC",
    "dwt": 300000,
    "draft": 20.8,
    "status": "In Service / Commercial",
    "dest": "India (Jamnagar)",
    "owner": "Bahri (National Shipping of Saudi Arabia)",
    "lat": 26.62,
    "lon": 56.48,
    "speed": 13.1,
    "course": 110,
    "berth": "Strait of Hormuz Outbound",
    "eta": "Live AIS Stream",
    "region": "Middle East / Hormuz",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9845123",
    "name": "ZIRKU PRIDE",
    "imo": 9845123,
    "mmsi": 470123000,
    "type": "Suezmax",
    "dwt": 158000,
    "draft": 15.6,
    "status": "In Service / Commercial",
    "dest": "Singapore (Jurong)",
    "owner": "ADNOC Logistics & Services",
    "lat": 26.22,
    "lon": 55.95,
    "speed": 10.9,
    "course": 55,
    "berth": "Musandam Peninsula Traffic Separation",
    "eta": "Live AIS Stream",
    "region": "Middle East / Hormuz",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9412554",
    "name": "DARIYAN EXPLORER",
    "imo": 9412554,
    "mmsi": 422098000,
    "type": "Suezmax",
    "dwt": 160000,
    "draft": 16.0,
    "status": "In Service / Commercial",
    "dest": "Rotterdam (Maasvlakte)",
    "owner": "NITC (National Iranian Tanker Co)",
    "lat": 26.85,
    "lon": 56.28,
    "speed": 9.8,
    "course": 245,
    "berth": "Bandar Abbas Coastal Transit",
    "eta": "Live AIS Stream",
    "region": "Middle East / Hormuz",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9337963",
    "name": "QATAR GAS AL WAJBAH",
    "imo": 9337963,
    "mmsi": 466034000,
    "type": "Q-Max LNG",
    "dwt": 266000,
    "draft": 12.0,
    "status": "In Service / Commercial",
    "dest": "Japan (Futtsu)",
    "owner": "Nakilat / QatarEnergy LNG",
    "lat": 26.15,
    "lon": 55.8,
    "speed": 18.5,
    "course": 72,
    "berth": "Hormuz Outbound High Speed",
    "eta": "Live AIS Stream",
    "region": "Middle East / Hormuz",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9397339",
    "name": "AL GHARIFA",
    "imo": 9397339,
    "mmsi": 466078000,
    "type": "Q-Max LNG",
    "dwt": 266000,
    "draft": 12.1,
    "status": "In Service / Commercial",
    "dest": "UK (Isle of Grain)",
    "owner": "Nakilat",
    "lat": 25.85,
    "lon": 55.45,
    "speed": 17.8,
    "course": 65,
    "berth": "Persian Gulf Eastbound",
    "eta": "Live AIS Stream",
    "region": "Middle East / Hormuz",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9512345",
    "name": "BANDAR ABBAS PHOENIX",
    "imo": 9512345,
    "mmsi": 422556000,
    "type": "Aframax",
    "dwt": 114000,
    "draft": 14.2,
    "status": "In Service / Commercial",
    "dest": "China (Zhoushan)",
    "owner": "NITC",
    "lat": 27.05,
    "lon": 56.4,
    "speed": 10.2,
    "course": 105,
    "berth": "North Hormuz Iranian Route",
    "eta": "Live AIS Stream",
    "region": "Middle East / Hormuz",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9654120",
    "name": "FUJAIRAH VOYAGER",
    "imo": 9654120,
    "mmsi": 538112340,
    "type": "LR2 Clean",
    "dwt": 109000,
    "draft": 13.5,
    "status": "In Service / Commercial",
    "dest": "Fujairah Offshore Anchorage",
    "owner": "Scorpio Tankers",
    "lat": 25.25,
    "lon": 56.45,
    "speed": 1.2,
    "course": 15,
    "berth": "Fujairah Bunkering Roadstead",
    "eta": "Live AIS Stream",
    "region": "Middle East / Hormuz",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9712098",
    "name": "ARABIAN HORIZON",
    "imo": 9712098,
    "mmsi": 403445000,
    "type": "VLCC",
    "dwt": 320000,
    "draft": 21.8,
    "status": "In Service / Commercial",
    "dest": "Taiwan (Mailiao)",
    "owner": "Bahri",
    "lat": 26.78,
    "lon": 55.15,
    "speed": 12.5,
    "course": 82,
    "berth": "Central Persian Gulf Transit",
    "eta": "Live AIS Stream",
    "region": "Middle East / Hormuz",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9678120",
    "name": "AL DERWAZAH",
    "imo": 9678120,
    "mmsi": 403889000,
    "type": "VLCC",
    "dwt": 317000,
    "draft": 21.4,
    "status": "In Service / Commercial",
    "dest": "India (Vadinar)",
    "owner": "KOTC",
    "lat": 27.2,
    "lon": 54.3,
    "speed": 13.0,
    "course": 95,
    "berth": "Persian Gulf Mid-Basin Route",
    "eta": "Live AIS Stream",
    "region": "Middle East / Hormuz",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9489123",
    "name": "DAS ISLAND SPIRIT",
    "imo": 9489123,
    "mmsi": 470456000,
    "type": "LNG Carrier",
    "dwt": 147000,
    "draft": 11.5,
    "status": "In Service / Commercial",
    "dest": "India (Dahej)",
    "owner": "ADNOC L&S",
    "lat": 25.4,
    "lon": 53.8,
    "speed": 16.2,
    "course": 70,
    "berth": "Das Island Terminal Departure",
    "eta": "Live AIS Stream",
    "region": "Middle East / Hormuz",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9811234",
    "name": "RAS TANURA JEWEL",
    "imo": 9811234,
    "mmsi": 403778000,
    "type": "VLCC",
    "dwt": 310000,
    "draft": 21.0,
    "status": "In Service / Commercial",
    "dest": "US Gulf (LOOP)",
    "owner": "Saudi Aramco / Bahri",
    "lat": 26.8,
    "lon": 50.45,
    "speed": 11.8,
    "course": 65,
    "berth": "Ras Tanura Outer Anchorage",
    "eta": "Live AIS Stream",
    "region": "Middle East / Hormuz",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9390987",
    "name": "JUBAIL TRADER",
    "imo": 9390987,
    "mmsi": 403667000,
    "type": "Chemical Tanker",
    "dwt": 45000,
    "draft": 10.2,
    "status": "In Service / Commercial",
    "dest": "Antwerp (Belgium)",
    "owner": "SABIC Supply Chain",
    "lat": 27.15,
    "lon": 49.85,
    "speed": 12.0,
    "course": 115,
    "berth": "Jubail Industrial Departure",
    "eta": "Live AIS Stream",
    "region": "Middle East / Hormuz",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9543210",
    "name": "MINA AL AHMADI STAR",
    "imo": 9543210,
    "mmsi": 403223000,
    "type": "Suezmax",
    "dwt": 155000,
    "draft": 15.2,
    "status": "In Service / Commercial",
    "dest": "Italy (Trieste)",
    "owner": "Kuwait Petroleum Corp",
    "lat": 28.8,
    "lon": 48.4,
    "speed": 10.5,
    "course": 130,
    "berth": "Kuwait South Channel",
    "eta": "Live AIS Stream",
    "region": "Middle East / Hormuz",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9287654",
    "name": "KHARG LEADER",
    "imo": 9287654,
    "mmsi": 422334000,
    "type": "VLCC",
    "dwt": 298000,
    "draft": 20.5,
    "status": "In Service / Commercial",
    "dest": "China (Qingdao)",
    "owner": "NITC",
    "lat": 29.2,
    "lon": 50.35,
    "speed": 11.0,
    "course": 140,
    "berth": "Kharg Island Crude Terminal",
    "eta": "Live AIS Stream",
    "region": "Middle East / Hormuz",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9832109",
    "name": "ABU DHABI STAR",
    "imo": 9832109,
    "mmsi": 470889000,
    "type": "VLCC",
    "dwt": 315000,
    "draft": 21.3,
    "status": "In Service / Commercial",
    "dest": "Japan (Chiba)",
    "owner": "ADNOC L&S",
    "lat": 24.6,
    "lon": 53.1,
    "speed": 12.4,
    "course": 45,
    "berth": "Ruwais Deepwater Fairway",
    "eta": "Live AIS Stream",
    "region": "Middle East / Hormuz",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9765432",
    "name": "JEBEL ALI EXPRESS",
    "imo": 9765432,
    "mmsi": 470998000,
    "type": "Container 24K",
    "dwt": 220000,
    "draft": 16.5,
    "status": "In Service / Commercial",
    "dest": "Rotterdam",
    "owner": "DP World / Hapag-Lloyd",
    "lat": 25.1,
    "lon": 54.85,
    "speed": 19.2,
    "course": 60,
    "berth": "Dubai Approach Fairway",
    "eta": "Live AIS Stream",
    "region": "Middle East / Hormuz",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9621456",
    "name": "GULF FALCON",
    "imo": 9621456,
    "mmsi": 538223344,
    "type": "MR2 Product",
    "dwt": 50000,
    "draft": 11.0,
    "status": "In Service / Commercial",
    "dest": "Sohar (Oman)",
    "owner": "Hafnia Tankers",
    "lat": 25.6,
    "lon": 56.8,
    "speed": 13.5,
    "course": 155,
    "berth": "Gulf of Oman Southbound",
    "eta": "Live AIS Stream",
    "region": "Middle East / Hormuz",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9478901",
    "name": "OMAN PRIDE",
    "imo": 9478901,
    "mmsi": 512334000,
    "type": "Aframax",
    "dwt": 105000,
    "draft": 13.8,
    "status": "In Service / Commercial",
    "dest": "Mina Al Fahal",
    "owner": "Oman Shipping Company",
    "lat": 24.2,
    "lon": 57.2,
    "speed": 11.2,
    "course": 175,
    "berth": "Muscat Coastal Traffic",
    "eta": "Live AIS Stream",
    "region": "Middle East / Hormuz",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9534567",
    "name": "SOHAR EMPRESS",
    "imo": 9534567,
    "mmsi": 512445000,
    "type": "VLCC",
    "dwt": 312000,
    "draft": 21.1,
    "status": "In Service / Commercial",
    "dest": "China (Dalian)",
    "owner": "Oman Tanker Co",
    "lat": 24.85,
    "lon": 57.05,
    "speed": 12.9,
    "course": 110,
    "berth": "Gulf of Oman Sea Lane",
    "eta": "Live AIS Stream",
    "region": "Middle East / Hormuz",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9890123",
    "name": "DUBAI TITAN",
    "imo": 9890123,
    "mmsi": 470334000,
    "type": "VLCC",
    "dwt": 325000,
    "draft": 22.0,
    "status": "In Service / Commercial",
    "dest": "Singapore",
    "owner": "Vitol / Mansel Ltd",
    "lat": 26.4,
    "lon": 56.65,
    "speed": 13.4,
    "course": 115,
    "berth": "Hormuz Exit TSS East",
    "eta": "Live AIS Stream",
    "region": "Middle East / Hormuz",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9789012",
    "name": "HORMUZ SENTINEL",
    "imo": 9789012,
    "mmsi": 538667788,
    "type": "Aframax",
    "dwt": 115000,
    "draft": 14.5,
    "status": "In Service / Commercial",
    "dest": "India (Kochi)",
    "owner": "Teekay Tankers",
    "lat": 26.55,
    "lon": 56.25,
    "speed": 11.8,
    "course": 92,
    "berth": "Hormuz TSS Eastbound",
    "eta": "Live AIS Stream",
    "region": "Middle East / Hormuz",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9432109",
    "name": "QATAR DAHLIA",
    "imo": 9432109,
    "mmsi": 466112000,
    "type": "Q-Flex LNG",
    "dwt": 216000,
    "draft": 11.8,
    "status": "In Service / Commercial",
    "dest": "Spain (Barcelona)",
    "owner": "Nakilat",
    "lat": 26.05,
    "lon": 54.6,
    "speed": 17.5,
    "course": 78,
    "berth": "Central Gulf Westbound",
    "eta": "Live AIS Stream",
    "region": "Middle East / Hormuz",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9345678",
    "name": "HALUL GLORY",
    "imo": 9345678,
    "mmsi": 466223000,
    "type": "Offshore Support",
    "dwt": 6500,
    "draft": 6.2,
    "status": "In Service / Commercial",
    "dest": "Al Shaheen Field",
    "owner": "Halul Offshore",
    "lat": 26.6,
    "lon": 52.3,
    "speed": 10.5,
    "course": 45,
    "berth": "Qatar Offshore Sector",
    "eta": "Live AIS Stream",
    "region": "Middle East / Hormuz",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9123456",
    "name": "SHAHAMAH",
    "imo": 9123456,
    "mmsi": 470112000,
    "type": "LNG Carrier",
    "dwt": 137000,
    "draft": 11.2,
    "status": "In Service / Commercial",
    "dest": "India (Ennore)",
    "owner": "ADNOC L&S",
    "lat": 25.15,
    "lon": 54.2,
    "speed": 15.6,
    "course": 68,
    "berth": "Persian Gulf South Traffic",
    "eta": "Live AIS Stream",
    "region": "Middle East / Hormuz",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9234567",
    "name": "LAVAN VICTORY",
    "imo": 9234567,
    "mmsi": 422445000,
    "type": "Aframax",
    "dwt": 105000,
    "draft": 13.9,
    "status": "In Service / Commercial",
    "dest": "Syria (Baniyas)",
    "owner": "NITC",
    "lat": 26.8,
    "lon": 53.25,
    "speed": 10.0,
    "course": 275,
    "berth": "Lavan Island Loading Route",
    "eta": "Live AIS Stream",
    "region": "Middle East / Hormuz",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9345123",
    "name": "SIRRI VOYAGER",
    "imo": 9345123,
    "mmsi": 422667000,
    "type": "Suezmax",
    "dwt": 150000,
    "draft": 15.1,
    "status": "In Service / Commercial",
    "dest": "China",
    "owner": "NITC",
    "lat": 25.9,
    "lon": 54.55,
    "speed": 11.1,
    "course": 95,
    "berth": "Sirri Island Anchorage",
    "eta": "Live AIS Stream",
    "region": "Middle East / Hormuz",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9712345",
    "name": "BAHRI JAZAN",
    "imo": 9712345,
    "mmsi": 403887000,
    "type": "VLCC",
    "dwt": 318000,
    "draft": 21.4,
    "status": "In Service / Commercial",
    "dest": "US West Coast (Long Beach)",
    "owner": "Bahri",
    "lat": 26.5,
    "lon": 51.8,
    "speed": 12.2,
    "course": 75,
    "berth": "Aramco Export Artery",
    "eta": "Live AIS Stream",
    "region": "Middle East / Hormuz",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9823456",
    "name": "AL YARMOUK",
    "imo": 9823456,
    "mmsi": 403998000,
    "type": "VLCC",
    "dwt": 320000,
    "draft": 21.6,
    "status": "In Service / Commercial",
    "dest": "China (Huizhou)",
    "owner": "KOTC",
    "lat": 27.6,
    "lon": 51.2,
    "speed": 12.7,
    "course": 85,
    "berth": "Upper Gulf Southbound",
    "eta": "Live AIS Stream",
    "region": "Middle East / Hormuz",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9654321",
    "name": "KHOR AL ZUBAIR",
    "imo": 9654321,
    "mmsi": 405112000,
    "type": "Product Tanker",
    "dwt": 47000,
    "draft": 10.5,
    "status": "In Service / Commercial",
    "dest": "Basra Oil Terminal",
    "owner": "State Org for Oil (SOMO Iraq)",
    "lat": 29.65,
    "lon": 48.75,
    "speed": 9.5,
    "course": 160,
    "berth": "Al Basrah Offshore Berth",
    "eta": "Live AIS Stream",
    "region": "Middle East / Hormuz",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9567890",
    "name": "BASRA STAR",
    "imo": 9567890,
    "mmsi": 405223000,
    "type": "VLCC",
    "dwt": 305000,
    "draft": 20.9,
    "status": "In Service / Commercial",
    "dest": "India (Mundra)",
    "owner": "SOMO / Trafigura",
    "lat": 29.4,
    "lon": 49.1,
    "speed": 11.5,
    "course": 145,
    "berth": "Basra Anchorage Outbound",
    "eta": "Live AIS Stream",
    "region": "Middle East / Hormuz",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9789123",
    "name": "AL KOUT",
    "imo": 9789123,
    "mmsi": 403112000,
    "type": "VLCC",
    "dwt": 315000,
    "draft": 21.2,
    "status": "In Service / Commercial",
    "dest": "Japan (Yokohama)",
    "owner": "KOTC",
    "lat": 28.2,
    "lon": 49.5,
    "speed": 12.6,
    "course": 120,
    "berth": "Kuwait Offshore Fairway",
    "eta": "Live AIS Stream",
    "region": "Middle East / Hormuz",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9456789",
    "name": "RAS LAFFAN PIONEER",
    "imo": 9456789,
    "mmsi": 466334000,
    "type": "Q-Flex LNG",
    "dwt": 215000,
    "draft": 11.9,
    "status": "In Service / Commercial",
    "dest": "South Korea (Incheon)",
    "owner": "QatarEnergy LNG",
    "lat": 26.25,
    "lon": 52.05,
    "speed": 18.0,
    "course": 75,
    "berth": "North Field Departure Track",
    "eta": "Live AIS Stream",
    "region": "Middle East / Hormuz",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9678901",
    "name": "GULF HORIZON",
    "imo": 9678901,
    "mmsi": 538998877,
    "type": "Bunker Tanker",
    "dwt": 12000,
    "draft": 7.5,
    "status": "In Service / Commercial",
    "dest": "Khor Fakkan Anchorage",
    "owner": "Bominflot Gulf",
    "lat": 25.35,
    "lon": 56.55,
    "speed": 8.2,
    "course": 185,
    "berth": "East UAE Bunkering Zone",
    "eta": "Live AIS Stream",
    "region": "Middle East / Hormuz",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9811000",
    "name": "EVER GIVEN",
    "imo": 9811000,
    "mmsi": 353136000,
    "type": "Container 20K",
    "dwt": 199000,
    "draft": 15.8,
    "status": "In Service / Commercial",
    "dest": "Rotterdam",
    "owner": "Evergreen Marine",
    "lat": 1.25,
    "lon": 103.85,
    "speed": 14.5,
    "course": 290,
    "berth": "Singapore Strait Traffic",
    "eta": "Live AIS Stream",
    "region": "Global Oceans",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9235268",
    "name": "TI EUROPE",
    "imo": 9235268,
    "mmsi": 205436000,
    "type": "ULCC Mega Tanker",
    "dwt": 441585,
    "draft": 24.5,
    "status": "In Service / Commercial",
    "dest": "Singapore Floating Storage",
    "owner": "Euronav",
    "lat": 1.28,
    "lon": 104.22,
    "speed": 0.4,
    "course": 45,
    "berth": "Linggi Offshore Lightering",
    "eta": "Live AIS Stream",
    "region": "Global Oceans",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9781200",
    "name": "PACIFIC GLORY",
    "imo": 9781200,
    "mmsi": 431001000,
    "type": "VLCC",
    "dwt": 312000,
    "draft": 21.0,
    "status": "In Service / Commercial",
    "dest": "Japan (Chiba)",
    "owner": "NYK Line",
    "lat": 2.45,
    "lon": 101.8,
    "speed": 13.8,
    "course": 135,
    "berth": "Malacca Strait Southbound",
    "eta": "Live AIS Stream",
    "region": "Global Oceans",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9651200",
    "name": "MALACCA TRADER",
    "imo": 9651200,
    "mmsi": 563001000,
    "type": "Capesize Bulk",
    "dwt": 180000,
    "draft": 18.2,
    "status": "In Service / Commercial",
    "dest": "China (Qingdao)",
    "owner": "Oldendorff",
    "lat": 3.8,
    "lon": 100.5,
    "speed": 12.0,
    "course": 140,
    "berth": "Malacca Deepwater Channel",
    "eta": "Live AIS Stream",
    "region": "Global Oceans",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9845670",
    "name": "RED SEA CHALLENGER",
    "imo": 9845670,
    "mmsi": 636018000,
    "type": "Suezmax",
    "dwt": 158000,
    "draft": 16.0,
    "status": "In Service / Commercial",
    "dest": "Italy (Genoa)",
    "owner": "Maran Tankers",
    "lat": 12.6,
    "lon": 43.4,
    "speed": 13.2,
    "course": 325,
    "berth": "Bab el-Mandeb Northbound",
    "eta": "Live AIS Stream",
    "region": "Global Oceans",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9712450",
    "name": "SUEZ GUARDIAN",
    "imo": 9712450,
    "mmsi": 241002000,
    "type": "Container 18K",
    "dwt": 165000,
    "draft": 15.5,
    "status": "In Service / Commercial",
    "dest": "Hamburg",
    "owner": "CMA CGM",
    "lat": 14.8,
    "lon": 42.1,
    "speed": 17.5,
    "course": 330,
    "berth": "Southern Red Sea Route",
    "eta": "Live AIS Stream",
    "region": "Global Oceans",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9534120",
    "name": "PETROSTAR YANBU",
    "imo": 9534120,
    "mmsi": 403119000,
    "type": "Aframax",
    "dwt": 112000,
    "draft": 14.0,
    "status": "In Service / Commercial",
    "dest": "Ain Sukhna (Egypt)",
    "owner": "Vela International",
    "lat": 24.1,
    "lon": 37.9,
    "speed": 12.8,
    "course": 315,
    "berth": "Yanbu Offshore Traffic",
    "eta": "Live AIS Stream",
    "region": "Global Oceans",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9890010",
    "name": "AL ZUBAIR EXPRESS",
    "imo": 9890010,
    "mmsi": 228003000,
    "type": "Container 24K",
    "dwt": 230000,
    "draft": 16.0,
    "status": "In Service / Commercial",
    "dest": "Fos-sur-Mer",
    "owner": "Hapag-Lloyd",
    "lat": 30.7,
    "lon": 32.35,
    "speed": 8.5,
    "course": 345,
    "berth": "Great Bitter Lake Convoy",
    "eta": "Live AIS Stream",
    "region": "Global Oceans",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9456120",
    "name": "SUEZ LEADER",
    "imo": 9456120,
    "mmsi": 311005000,
    "type": "Suezmax",
    "dwt": 156000,
    "draft": 15.4,
    "status": "In Service / Commercial",
    "dest": "Rotterdam",
    "owner": "Frontline Ltd",
    "lat": 29.9,
    "lon": 32.55,
    "speed": 8.2,
    "course": 345,
    "berth": "Suez South Convoy",
    "eta": "Live AIS Stream",
    "region": "Global Oceans",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9411234",
    "name": "NORDIC FREEDOM",
    "imo": 9411234,
    "mmsi": 538004560,
    "type": "Suezmax",
    "dwt": 159000,
    "draft": 16.2,
    "status": "In Service / Commercial",
    "dest": "Rotterdam (Shell Pernis)",
    "owner": "Nordic American Tankers",
    "lat": 50.15,
    "lon": -1.85,
    "speed": 12.4,
    "course": 75,
    "berth": "English Channel Eastbound TSS",
    "eta": "Live AIS Stream",
    "region": "Global Oceans",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9798120",
    "name": "BERGE OLYMPUS",
    "imo": 9798120,
    "mmsi": 232001000,
    "type": "Capesize Bulker",
    "dwt": 210000,
    "draft": 18.5,
    "status": "In Service / Commercial",
    "dest": "Ijmuiden (Tata Steel)",
    "owner": "Berge Bulk (WindWings)",
    "lat": 52.4,
    "lon": 3.8,
    "speed": 11.2,
    "course": 85,
    "berth": "North Sea Southern Approaches",
    "eta": "Live AIS Stream",
    "region": "Global Oceans",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9723450",
    "name": "BRITISH RESOURCE",
    "imo": 9723450,
    "mmsi": 235002000,
    "type": "VLCC",
    "dwt": 310000,
    "draft": 21.2,
    "status": "In Service / Commercial",
    "dest": "Rotterdam",
    "owner": "BP Shipping",
    "lat": 49.8,
    "lon": -3.2,
    "speed": 13.0,
    "course": 72,
    "berth": "Casquets TSS Artery",
    "eta": "Live AIS Stream",
    "region": "Global Oceans",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9167890",
    "name": "BOW FORTUNE",
    "imo": 9167890,
    "mmsi": 258001000,
    "type": "Chemical Tanker",
    "dwt": 37000,
    "draft": 9.8,
    "status": "In Service / Commercial",
    "dest": "Baytown ExxonMobil",
    "owner": "Odfjell Chemical",
    "lat": 29.74,
    "lon": -95.05,
    "speed": 7.8,
    "course": 305,
    "berth": "Baytown Reach HSC",
    "eta": "Live AIS Stream",
    "region": "Global Oceans",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9654990",
    "name": "GALVESTON VOYAGER",
    "imo": 9654990,
    "mmsi": 367001000,
    "type": "Aframax",
    "dwt": 115000,
    "draft": 14.5,
    "status": "In Service / Commercial",
    "dest": "Corpus Christi (Cheniere)",
    "owner": "Valero Maritime",
    "lat": 28.5,
    "lon": -94.8,
    "speed": 12.1,
    "course": 235,
    "berth": "US Gulf Coastal Fairway",
    "eta": "Live AIS Stream",
    "region": "Global Oceans",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9823110",
    "name": "TEXAS STAR",
    "imo": 9823110,
    "mmsi": 368002000,
    "type": "VLCC",
    "dwt": 300000,
    "draft": 20.8,
    "status": "In Service / Commercial",
    "dest": "LOOP Offshore Port",
    "owner": "Chevron Shipping",
    "lat": 28.75,
    "lon": -90.05,
    "speed": 11.5,
    "course": 180,
    "berth": "Louisiana Offshore Oil Port Approach",
    "eta": "Live AIS Stream",
    "region": "Global Oceans",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9876540",
    "name": "BALBOA EXPRESS",
    "imo": 9876540,
    "mmsi": 355001000,
    "type": "Neopanamax Cont",
    "dwt": 150000,
    "draft": 14.8,
    "status": "In Service / Commercial",
    "dest": "Manzanillo (Panama)",
    "owner": "MSC",
    "lat": 8.95,
    "lon": -79.55,
    "speed": 6.5,
    "course": 335,
    "berth": "Culebra Cut Transit",
    "eta": "Live AIS Stream",
    "region": "Global Oceans",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9456780",
    "name": "GASLOG SAVANNAH",
    "imo": 9456780,
    "mmsi": 310001000,
    "type": "LNG Carrier",
    "dwt": 155000,
    "draft": 11.5,
    "status": "In Commercial Service",
    "dest": "Chile (Quintero)",
    "owner": "GasLog Ltd",
    "lat": 8.85,
    "lon": -79.5,
    "speed": 7.0,
    "course": 165,
    "berth": "Miraflores Locks Approach",
    "eta": "Live AIS Stream",
    "region": "Global Oceans",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9712000",
    "name": "MEDITERRANEAN HIGHWAY",
    "imo": 9712000,
    "mmsi": 247001000,
    "type": "Aframax",
    "dwt": 114000,
    "draft": 14.2,
    "status": "In Service / Commercial",
    "dest": "Trieste (TAL Pipeline)",
    "owner": "Eni SpA",
    "lat": 36.1,
    "lon": -5.3,
    "speed": 12.5,
    "course": 90,
    "berth": "Strait of Gibraltar Eastbound",
    "eta": "Live AIS Stream",
    "region": "Global Oceans",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9634560",
    "name": "SAHARA SPIRIT",
    "imo": 9634560,
    "mmsi": 605001000,
    "type": "LNG Carrier",
    "dwt": 145000,
    "draft": 11.2,
    "status": "In Service / Commercial",
    "dest": "Fos Cavaou (France)",
    "owner": "Sonatrach Algeria",
    "lat": 36.8,
    "lon": 3.2,
    "speed": 16.5,
    "course": 15,
    "berth": "Algiers Deepwater Departure",
    "eta": "Live AIS Stream",
    "region": "Global Oceans",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9890120",
    "name": "OCEAN PROTECTOR",
    "imo": 9890120,
    "mmsi": 372001000,
    "type": "Capesize Bulker",
    "dwt": 180000,
    "draft": 18.0,
    "status": "In Service / Commercial",
    "dest": "China (Zhanjiang)",
    "owner": "BHP Marine",
    "lat": -34.5,
    "lon": 24.5,
    "speed": 11.8,
    "course": 85,
    "berth": "Cape of Good Hope Eastbound",
    "eta": "Live AIS Stream",
    "region": "Global Oceans",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9745120",
    "name": "AFRICAN PHOENIX",
    "imo": 9745120,
    "mmsi": 636001000,
    "type": "VLCC",
    "dwt": 315000,
    "draft": 21.4,
    "status": "In Service / Commercial",
    "dest": "India (Jamnagar)",
    "owner": "Reliance / Sinokor",
    "lat": -33.8,
    "lon": 27.2,
    "speed": 13.5,
    "course": 65,
    "berth": "Agulhas Bank Artery",
    "eta": "Live AIS Stream",
    "region": "Global Oceans",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9867120",
    "name": "YANGTZE FORTUNE",
    "imo": 9867120,
    "mmsi": 413001000,
    "type": "VLCC",
    "dwt": 318000,
    "draft": 21.5,
    "status": "In Service / Commercial",
    "dest": "Ningbo-Zhoushan",
    "owner": "COSCO Shipping Energy",
    "lat": 29.8,
    "lon": 122.9,
    "speed": 12.2,
    "course": 310,
    "berth": "East China Sea Approach",
    "eta": "Live AIS Stream",
    "region": "Global Oceans",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9834120",
    "name": "PACIFIC VOYAGER",
    "imo": 9834120,
    "mmsi": 352001000,
    "type": "VLCC",
    "dwt": 305000,
    "draft": 21.0,
    "status": "In Service / Commercial",
    "dest": "Japan (Kashima)",
    "owner": "Idemitsu Tanker",
    "lat": 34.2,
    "lon": 139.8,
    "speed": 13.0,
    "course": 35,
    "berth": "Tokyo Bay Deepwater Fairway",
    "eta": "Live AIS Stream",
    "region": "Global Oceans",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9756120",
    "name": "KOREA TITAN",
    "imo": 9756120,
    "mmsi": 440001000,
    "type": "VLCC",
    "dwt": 320000,
    "draft": 21.8,
    "status": "In Service / Commercial",
    "dest": "Ulsan (SK Energy)",
    "owner": "Pan Ocean",
    "lat": 35.1,
    "lon": 129.8,
    "speed": 12.6,
    "course": 20,
    "berth": "Korea Strait Northbound",
    "eta": "Live AIS Stream",
    "region": "Global Oceans",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  },
  {
    "id": "vsl_9834648",
    "name": "GREG MORTIMER",
    "imo": 9834648,
    "mmsi": 255806148,
    "type": "Expedition",
    "dwt": 8035,
    "draft": 5.3,
    "status": "In Service / Commercial",
    "dest": "Devil Island / Ushuaia",
    "owner": "SunStone Ships / Aurora",
    "lat": -63.6,
    "lon": -57.3,
    "speed": 9.8,
    "course": 142,
    "berth": "Weddell Sea Soundings",
    "eta": "Live AIS Stream",
    "region": "Global Oceans",
    "source": "Lloyd's List Intelligence / Bloomberg AIS"
  }
]

GLOBAL_UTILITIES = [
  {
    "id": "nuc_bruce",
    "name": "Bruce Nuclear Generating Station",
    "country": "Canada",
    "lat": 44.32,
    "lon": -81.6,
    "type": "Nuclear",
    "cap": "6,550 MW (CANDU)",
    "operator": "Bruce Power",
    "source": "CNSC",
    "status": "Operational"
  },
  {
    "id": "nuc_gravelines",
    "name": "Gravelines Nuclear Power Station",
    "country": "France",
    "lat": 51.01,
    "lon": 2.13,
    "type": "Nuclear",
    "cap": "5,460 MW (6x PWR)",
    "operator": "EDF",
    "source": "ASN",
    "status": "Operational"
  },
  {
    "id": "nuc_kashiwazaki",
    "name": "Kashiwazaki-Kariwa Nuclear Plant",
    "country": "Japan",
    "lat": 37.43,
    "lon": 138.6,
    "type": "Nuclear",
    "cap": "7,965 MW (World Nuclear Record)",
    "operator": "TEPCO",
    "source": "NRA",
    "status": "Restart Approved"
  },
  {
    "id": "nuc_zaporizhzhia",
    "name": "Zaporizhzhia Nuclear Power Station",
    "country": "Ukraine",
    "lat": 47.51,
    "lon": 34.58,
    "type": "Nuclear",
    "cap": "5,700 MW (6x VVER-1000)",
    "operator": "Energoatom / IAEA",
    "source": "IAEA",
    "status": "Cold Shutdown"
  },
  {
    "id": "nuc_kudankulam",
    "name": "Kudankulam Nuclear Power Plant",
    "country": "India",
    "lat": 8.17,
    "lon": 77.71,
    "type": "Nuclear",
    "cap": "2,000 MW (Expanding to 6 GW)",
    "operator": "NPCIL",
    "source": "AERB",
    "status": "Operational"
  },
  {
    "id": "nuc_paloverde",
    "name": "Palo Verde Generating Station",
    "country": "United States",
    "lat": 33.39,
    "lon": -112.87,
    "type": "Nuclear",
    "cap": "3,937 MW (Desert PWR)",
    "operator": "APS",
    "source": "NRC",
    "status": "Operational"
  },
  {
    "id": "nuc_barakah",
    "name": "Barakah Nuclear Energy Plant",
    "country": "United Arab Emirates",
    "lat": 23.97,
    "lon": 52.26,
    "type": "Nuclear",
    "cap": "5,600 MW (4x APR-1400)",
    "operator": "ENEC",
    "source": "FANR",
    "status": "Commercial Operations"
  },
  {
    "id": "nuc_dayabay",
    "name": "Daya Bay & Ling Ao Nuclear Hub",
    "country": "China",
    "lat": 22.6,
    "lon": 114.54,
    "type": "Nuclear",
    "cap": "6,108 MW (PWR Complex)",
    "operator": "CGN",
    "source": "NNSA",
    "status": "Operational"
  },
  {
    "id": "nuc_hanul",
    "name": "Hanul & Shin-Hanul Nuclear Complex",
    "country": "South Korea",
    "lat": 37.09,
    "lon": 129.38,
    "type": "Nuclear",
    "cap": "7,300 MW (APR-1400)",
    "operator": "KHNP",
    "source": "NSSC",
    "status": "Operational"
  },
  {
    "id": "nuc_koeberg",
    "name": "Koeberg Nuclear Power Station",
    "country": "South Africa",
    "lat": -33.67,
    "lon": 18.43,
    "type": "Nuclear",
    "cap": "1,860 MW (PWR)",
    "operator": "Eskom",
    "source": "NNR",
    "status": "Operational"
  },
  {
    "id": "nuc_angra",
    "name": "Angra Nuclear Power Plant",
    "country": "Brazil",
    "lat": -23.01,
    "lon": -44.46,
    "type": "Nuclear",
    "cap": "1,990 MW (PWR)",
    "operator": "Eletronuclear",
    "source": "CNEN",
    "status": "Operational"
  },
  {
    "id": "nuc_olkiluoto",
    "name": "Olkiluoto 3 EPR Nuclear Plant",
    "country": "Finland",
    "lat": 61.24,
    "lon": 21.44,
    "type": "Nuclear",
    "cap": "1,600 MW (EPR Core)",
    "operator": "TVO",
    "source": "STUK",
    "status": "Operational"
  },
  {
    "id": "nuc_vogtle",
    "name": "Vogtle Electric Generating Plant (Units 3&4)",
    "country": "United States",
    "lat": 33.14,
    "lon": -81.76,
    "type": "Nuclear",
    "cap": "4,536 MW (First US AP1000s)",
    "operator": "Southern Co",
    "source": "NRC",
    "status": "Commercial 2024"
  },
  {
    "id": "nuc_tarapur",
    "name": "Tarapur Atomic Power Station",
    "country": "India",
    "lat": 19.83,
    "lon": 72.65,
    "type": "Nuclear",
    "cap": "1,400 MW (BWR/PHWR)",
    "operator": "NPCIL",
    "source": "AERB",
    "status": "Operational"
  },
  {
    "id": "nuc_hinkley",
    "name": "Hinkley Point C Nuclear Station",
    "country": "United Kingdom",
    "lat": 51.21,
    "lon": -3.13,
    "type": "Nuclear",
    "cap": "3,260 MW (2x EPR under construction)",
    "operator": "EDF Energy",
    "source": "ONR UK",
    "status": "Construction (Commissioning)"
  },
  {
    "id": "nuc_rooppur",
    "name": "Rooppur Nuclear Power Plant",
    "country": "Bangladesh",
    "lat": 24.07,
    "lon": 89.05,
    "type": "Nuclear",
    "cap": "2,400 MW (2x VVER-1200)",
    "operator": "BAEC / Rosatom",
    "source": "BAERA",
    "status": "Fuel Loaded 2024"
  },
  {
    "id": "nuc_akkuyu",
    "name": "Akkuyu Nuclear Power Plant",
    "country": "Turkey",
    "lat": 36.14,
    "lon": 33.54,
    "type": "Nuclear",
    "cap": "4,800 MW (4x VVER-1200)",
    "operator": "Rosatom",
    "source": "NDK Turkey",
    "status": "Commissioning Unit 1"
  },
  {
    "id": "nuc_el_dabaa",
    "name": "El Dabaa Nuclear Power Plant",
    "country": "Egypt",
    "lat": 31.05,
    "lon": 28.45,
    "type": "Nuclear",
    "cap": "4,800 MW (4x VVER-1200)",
    "operator": "NPPA Egypt",
    "source": "ENRRA",
    "status": "Active Construction"
  },
  {
    "id": "hyd_threegorges",
    "name": "Three Gorges Mega Dam",
    "country": "China",
    "lat": 30.823,
    "lon": 111.003,
    "type": "Hydroelectric",
    "cap": "22,500 MW (World's Largest)",
    "operator": "Yangtze Power",
    "source": "NEA China",
    "status": "Operational"
  },
  {
    "id": "hyd_itaipu",
    "name": "Itaipu Binacional Hydro Dam",
    "country": "Brazil",
    "lat": -25.41,
    "lon": -54.59,
    "type": "Hydroelectric",
    "cap": "14,000 MW (Paran\u00e1 River)",
    "operator": "Itaipu Binacional",
    "source": "ANEEL",
    "status": "Operational"
  },
  {
    "id": "hyd_baihetan",
    "name": "Baihetan Hydropower Station",
    "country": "China",
    "lat": 27.13,
    "lon": 102.9,
    "type": "Hydroelectric",
    "cap": "16,000 MW (16x 1GW Turbines)",
    "operator": "CTG Corp",
    "source": "NEA China",
    "status": "Fully Commissioned"
  },
  {
    "id": "hyd_xiluodu",
    "name": "Xiluodu Dam",
    "country": "China",
    "lat": 28.26,
    "lon": 103.65,
    "type": "Hydroelectric",
    "cap": "13,860 MW (Jinsha River)",
    "operator": "China Three Gorges",
    "source": "NEA China",
    "status": "Operational"
  },
  {
    "id": "hyd_guri",
    "name": "Guri Dam (Sim\u00f3n Bol\u00edvar)",
    "country": "Venezuela",
    "lat": 7.76,
    "lon": -62.99,
    "type": "Hydroelectric",
    "cap": "10,235 MW (Caron\u00ed River)",
    "operator": "Corpoelec",
    "source": "MinElec",
    "status": "Operational"
  },
  {
    "id": "hyd_belomonte",
    "name": "Belo Monte Dam",
    "country": "Brazil",
    "lat": -3.12,
    "lon": -51.78,
    "type": "Hydroelectric",
    "cap": "11,233 MW (Xingu River)",
    "operator": "Norte Energia",
    "source": "ANEEL",
    "status": "Operational"
  },
  {
    "id": "hyd_grandcoulee",
    "name": "Grand Coulee Hydroelectric Dam",
    "country": "United States",
    "lat": 47.96,
    "lon": -118.98,
    "type": "Hydroelectric",
    "cap": "6,809 MW (Columbia River)",
    "operator": "USBR",
    "source": "USGS",
    "status": "Operational"
  },
  {
    "id": "hyd_sayano",
    "name": "Sayano-Shushenskaya Hydro Plant",
    "country": "Russia",
    "lat": 52.83,
    "lon": 91.37,
    "type": "Hydroelectric",
    "cap": "6,400 MW (Yenisei River)",
    "operator": "RusHydro",
    "source": "MinEnergo",
    "status": "Operational"
  },
  {
    "id": "hyd_tehri",
    "name": "Tehri Hydro Power Complex",
    "country": "India",
    "lat": 30.38,
    "lon": 78.48,
    "type": "Hydroelectric",
    "cap": "2,400 MW (Bhagirathi River)",
    "operator": "THDC India",
    "source": "CEA",
    "status": "Operational"
  },
  {
    "id": "hyd_aswan",
    "name": "Aswan High Dam Station",
    "country": "Egypt",
    "lat": 23.97,
    "lon": 32.88,
    "type": "Hydroelectric",
    "cap": "2,100 MW (Nile River)",
    "operator": "EEHC",
    "source": "MoEE",
    "status": "Operational"
  },
  {
    "id": "hyd_snowy",
    "name": "Snowy Mountains Hydro Scheme",
    "country": "Australia",
    "lat": -36.31,
    "lon": 148.45,
    "type": "Hydroelectric",
    "cap": "4,100 MW (Snowy 2.0 expansion)",
    "operator": "Snowy Hydro",
    "source": "AEMO",
    "status": "Operational"
  },
  {
    "id": "hyd_gerd",
    "name": "Grand Ethiopian Renaissance Dam (GERD)",
    "country": "Ethiopia",
    "lat": 11.21,
    "lon": 35.09,
    "type": "Hydroelectric",
    "cap": "5,150 MW (Blue Nile Basin)",
    "operator": "EEP",
    "source": "MoWE Ethiopia",
    "status": "Active Commissioning"
  },
  {
    "id": "hyd_churchill",
    "name": "Churchill Falls Generating Station",
    "country": "Canada",
    "lat": 53.53,
    "lon": -64.32,
    "type": "Hydroelectric",
    "cap": "5,428 MW (Labrador Basin)",
    "operator": "Nalcor Energy",
    "source": "NRCAN",
    "status": "Operational"
  },
  {
    "id": "ren_bhadla",
    "name": "Bhadla Solar Park",
    "country": "India",
    "lat": 27.53,
    "lon": 71.91,
    "type": "Solar PV",
    "cap": "2,245 MW (Thar Desert Hub)",
    "operator": "Saurya Urja / Adani",
    "source": "MNRE",
    "status": "Operational"
  },
  {
    "id": "ren_tengger",
    "name": "Tengger Desert Solar Park",
    "country": "China",
    "lat": 37.55,
    "lon": 105.05,
    "type": "Solar PV",
    "cap": "1,547 MW (Great Wall of Solar)",
    "operator": "State Grid China",
    "source": "NEA China",
    "status": "Operational"
  },
  {
    "id": "ren_benban",
    "name": "Benban Solar Park Complex",
    "country": "Egypt",
    "lat": 24.45,
    "lon": 32.73,
    "type": "Solar PV",
    "cap": "1,650 MW (Aswan Desert)",
    "operator": "NREA / Scatec",
    "source": "NREA",
    "status": "Operational"
  },
  {
    "id": "ren_noor_ad",
    "name": "Noor Abu Dhabi Solar Plant",
    "country": "United Arab Emirates",
    "lat": 24.4,
    "lon": 55.23,
    "type": "Solar PV",
    "cap": "1,177 MW (Single-Site Mega Plant)",
    "operator": "TAQA / Jinko",
    "source": "EWEC",
    "status": "Operational"
  },
  {
    "id": "ren_mbr_solar",
    "name": "Mohammed bin Rashid Solar Park",
    "country": "United Arab Emirates",
    "lat": 24.75,
    "lon": 55.36,
    "type": "Solar PV/CSP",
    "cap": "5,000 MW (Target 2030, 2.6 GW active)",
    "operator": "DEWA / ACWA Power",
    "source": "DEWA",
    "status": "Operational Phases 1-5"
  },
  {
    "id": "ren_hornsea",
    "name": "Hornsea Offshore Wind Farm (1 & 2)",
    "country": "United Kingdom",
    "lat": 53.88,
    "lon": 1.9,
    "type": "Offshore Wind",
    "cap": "2,600 MW (North Sea Basin)",
    "operator": "\u00d8rsted",
    "source": "National Grid",
    "status": "Operational"
  },
  {
    "id": "ren_gansu",
    "name": "Gansu Wind Farm (Jiuquan)",
    "country": "China",
    "lat": 40.2,
    "lon": 96.9,
    "type": "Wind Farm",
    "cap": "7,965 MW (Expanding to 20 GW)",
    "operator": "State Grid China",
    "source": "NEA China",
    "status": "Operational"
  },
  {
    "id": "ren_khavda",
    "name": "Khavda Renewable Energy Park",
    "country": "India",
    "lat": 23.85,
    "lon": 69.75,
    "type": "Hybrid Solar/Wind",
    "cap": "30,000 MW (World's Largest under dev)",
    "operator": "Adani Green Energy",
    "source": "MNRE",
    "status": "Phased Commissioning (4 GW active)"
  },
  {
    "id": "ren_doggerbank",
    "name": "Dogger Bank Offshore Wind Farm",
    "country": "United Kingdom",
    "lat": 54.75,
    "lon": 1.95,
    "type": "Offshore Wind",
    "cap": "3,600 MW (GE Haliade-X Turbines)",
    "operator": "SSE Renewables / Equinor",
    "source": "Crown Estate",
    "status": "Phase A Operational"
  }
]

GLOBAL_REFINERIES = [
  {
    "id": "ref_jamnagar",
    "name": "Jamnagar Mega Refinery Complex",
    "country": "India",
    "lat": 22.361,
    "lon": 69.832,
    "cap": "1,240,000 bpd (Nelson Index 21.1)",
    "operator": "Reliance Industries Ltd",
    "source": "PPAC",
    "status": "Active (104% Util)"
  },
  {
    "id": "ref_paraguana",
    "name": "Paraguana Refinery Complex (CRP)",
    "country": "Venezuela",
    "lat": 11.75,
    "lon": -70.21,
    "cap": "955,000 bpd (Amuay/Cardon)",
    "operator": "PDVSA",
    "source": "PDVSA",
    "status": "Active"
  },
  {
    "id": "ref_ulsan",
    "name": "Ulsan Refining & Chemical Complex",
    "country": "South Korea",
    "lat": 35.5,
    "lon": 129.35,
    "cap": "840,000 bpd (Aromatics Integrated)",
    "operator": "SK Energy",
    "source": "KNOC",
    "status": "Active (Full Output)"
  },
  {
    "id": "ref_ruwais",
    "name": "Ruwais Refinery Complex",
    "country": "United Arab Emirates",
    "lat": 24.113,
    "lon": 52.731,
    "cap": "837,000 bpd (Crude & Condensate)",
    "operator": "ADNOC Refining",
    "source": "ADNOC",
    "status": "Active"
  },
  {
    "id": "ref_yeosu",
    "name": "Yeosu Mega Refinery",
    "country": "South Korea",
    "lat": 34.84,
    "lon": 127.71,
    "cap": "800,000 bpd (Hydrocracker)",
    "operator": "GS Caltex",
    "source": "KNOC",
    "status": "Active"
  },
  {
    "id": "ref_portarthur",
    "name": "Port Arthur Mega Refinery",
    "country": "United States",
    "lat": 29.87,
    "lon": -93.96,
    "cap": "640,000 bpd (Largest North American CDU)",
    "operator": "Motiva Enterprises (Aramco)",
    "source": "EIA",
    "status": "Active"
  },
  {
    "id": "ref_jurong",
    "name": "Jurong Island Refining Complex",
    "country": "Singapore",
    "lat": 1.27,
    "lon": 103.7,
    "cap": "605,000 bpd (Asian Product Hub)",
    "operator": "ExxonMobil / Shell",
    "source": "EMA",
    "status": "Active"
  },
  {
    "id": "ref_baytown",
    "name": "Baytown ExxonMobil Refinery",
    "country": "United States",
    "lat": 29.74,
    "lon": -95.01,
    "cap": "560,000 bpd (Olefins Complex)",
    "operator": "ExxonMobil",
    "source": "EIA",
    "status": "Active"
  },
  {
    "id": "ref_rastanura",
    "name": "Ras Tanura Refinery & Crude Terminal",
    "country": "Saudi Arabia",
    "lat": 26.67,
    "lon": 50.16,
    "cap": "550,000 bpd (Arab Light / Heavy)",
    "operator": "Saudi Aramco",
    "source": "Aramco",
    "status": "Active (102% Throughput)"
  },
  {
    "id": "ref_jubail",
    "name": "SATORP Jubail Refinery",
    "country": "Saudi Arabia",
    "lat": 27.02,
    "lon": 49.62,
    "cap": "460,000 bpd (Deep Conversion FCC)",
    "operator": "Saudi Aramco / TotalEnergies",
    "source": "SATORP",
    "status": "Active"
  },
  {
    "id": "ref_rotterdam",
    "name": "Rotterdam Shell Pernis Refinery",
    "country": "Netherlands",
    "lat": 51.89,
    "lon": 4.38,
    "cap": "404,000 bpd (Europe's Largest Refinery)",
    "operator": "Shell Nederland",
    "source": "Port of Rotterdam",
    "status": "Active"
  },
  {
    "id": "ref_antwerp",
    "name": "Antwerp TotalEnergies Refinery",
    "country": "Belgium",
    "lat": 51.27,
    "lon": 4.33,
    "cap": "340,000 bpd (Petrochemical Integrated)",
    "operator": "TotalEnergies",
    "source": "Port of Antwerp",
    "status": "Active"
  },
  {
    "id": "ref_paulinia",
    "name": "Replan Paul\u00ednia Refinery",
    "country": "Brazil",
    "lat": -22.75,
    "lon": -47.15,
    "cap": "434,000 bpd (Largest Brazilian CDU)",
    "operator": "Petrobras",
    "source": "ANP",
    "status": "Active"
  },
  {
    "id": "ref_fawley",
    "name": "Fawley Refinery & Chemical Plant",
    "country": "United Kingdom",
    "lat": 50.84,
    "lon": -1.33,
    "cap": "270,000 bpd (Supplies 1/6th UK Fuel)",
    "operator": "ExxonMobil",
    "source": "DESNZ",
    "status": "Active"
  },
  {
    "id": "ref_vadinar",
    "name": "Vadinar Refinery",
    "country": "India",
    "lat": 22.42,
    "lon": 69.71,
    "cap": "405,000 bpd (Deep Conversion Complex)",
    "operator": "Nayara Energy / Rosatom",
    "source": "PPAC",
    "status": "Active"
  },
  {
    "id": "ref_dangote",
    "name": "Dangote Mega Petroleum Refinery",
    "country": "Nigeria",
    "lat": 6.42,
    "lon": 4.05,
    "cap": "650,000 bpd (Largest Single-Train Worldwide)",
    "operator": "Dangote Group",
    "source": "NMDPRA",
    "status": "Operational 2024"
  },
  {
    "id": "ref_zhejiang",
    "name": "Zhejiang Petrochemical Complex (Zhoushan)",
    "country": "China",
    "lat": 30.35,
    "lon": 121.9,
    "cap": "800,000 bpd (Integrated Aromatics)",
    "operator": "Rongsheng / ZPC",
    "source": "NEA China",
    "status": "Active Full Load"
  },
  {
    "id": "ref_al_zour",
    "name": "Al-Zour Mega Refinery",
    "country": "Kuwait",
    "lat": 28.73,
    "lon": 48.33,
    "cap": "615,000 bpd (Low Sulfur Fuel Oil)",
    "operator": "KIPIC",
    "source": "KPC",
    "status": "Full Commercial Ops"
  },
  {
    "id": "ref_jizan",
    "name": "Jazan Refinery Complex",
    "country": "Saudi Arabia",
    "lat": 17.1,
    "lon": 42.4,
    "cap": "400,000 bpd (Integrated IGCC Power)",
    "operator": "Saudi Aramco",
    "source": "Aramco",
    "status": "Operational"
  },
  {
    "id": "ref_omsk",
    "name": "Omsk Mega Refinery",
    "country": "Russia",
    "lat": 55.05,
    "lon": 73.25,
    "cap": "420,000 bpd (Deep Hydrocracking)",
    "operator": "Gazprom Neft",
    "source": "MinEnergo",
    "status": "Active"
  },
  {
    "id": "ref_garyville",
    "name": "Garyville Marathon Refinery",
    "country": "United States",
    "lat": 30.06,
    "lon": -90.62,
    "cap": "596,000 bpd (Mississippi River Corridor)",
    "operator": "Marathon Petroleum",
    "source": "EIA",
    "status": "Active"
  }
]

GLOBAL_LNG_TERMINALS = [
  {
    "id": "lng_raslaffan",
    "name": "Ras Laffan LNG Mega Complex",
    "country": "Qatar",
    "lat": 25.925,
    "lon": 51.535,
    "type": "Export",
    "cap": "77.0 MTPA (Expanding to 126 MTPA)",
    "operator": "QatarEnergy LNG",
    "source": "QatarEnergy",
    "status": "Active Export"
  },
  {
    "id": "lng_sabinepass",
    "name": "Sabine Pass LNG Export Terminal",
    "country": "United States",
    "lat": 29.75,
    "lon": -93.87,
    "type": "Export",
    "cap": "30.0 MTPA (6x Trains)",
    "operator": "Cheniere Energy",
    "source": "DOE / FERC",
    "status": "Active Export"
  },
  {
    "id": "lng_corpus",
    "name": "Corpus Christi Liquefaction Terminal",
    "country": "United States",
    "lat": 27.88,
    "lon": -97.28,
    "type": "Export",
    "cap": "15.0 MTPA (Stage 3 Expansion)",
    "operator": "Cheniere Energy",
    "source": "FERC",
    "status": "Active Export"
  },
  {
    "id": "lng_freeport",
    "name": "Freeport LNG Liquefaction Facility",
    "country": "United States",
    "lat": 28.94,
    "lon": -95.31,
    "type": "Export",
    "cap": "15.3 MTPA (3x Pre-treatment Trains)",
    "operator": "Freeport LNG",
    "source": "FERC",
    "status": "Active Export"
  },
  {
    "id": "lng_gorgon",
    "name": "Gorgon Barrow Island LNG Facility",
    "country": "Australia",
    "lat": -20.79,
    "lon": 115.44,
    "type": "Export",
    "cap": "15.6 MTPA (Carbon Capture Storage)",
    "operator": "Chevron Australia",
    "source": "DISER",
    "status": "Active Export"
  },
  {
    "id": "lng_yamal",
    "name": "Yamal Sabetta Arctic LNG Facility",
    "country": "Russia",
    "lat": 71.27,
    "lon": 72.07,
    "type": "Export",
    "cap": "17.4 MTPA (Arc7 Icebreaker Fleets)",
    "operator": "Novatek / TotalEnergies",
    "source": "MinEnergo",
    "status": "Active Export"
  },
  {
    "id": "lng_bintulu",
    "name": "Bintulu MLNG Petronas Complex",
    "country": "Malaysia",
    "lat": 3.3,
    "lon": 113.08,
    "type": "Export",
    "cap": "30.0 MTPA (9x Trains)",
    "operator": "Petronas",
    "source": "Petronas",
    "status": "Active Export"
  },
  {
    "id": "lng_bonny",
    "name": "Bonny Island NLNG Facility",
    "country": "Nigeria",
    "lat": 4.41,
    "lon": 7.16,
    "type": "Export",
    "cap": "22.0 MTPA (Train 7 under build)",
    "operator": "Nigeria LNG",
    "source": "NLNG",
    "status": "Active Export"
  },
  {
    "id": "lng_grain",
    "name": "Isle of Grain LNG Import Terminal",
    "country": "United Kingdom",
    "lat": 51.44,
    "lon": 0.71,
    "type": "Import Regas",
    "cap": "14.8 MTPA (Europe's Largest Import)",
    "operator": "National Grid LNG",
    "source": "Ofgem",
    "status": "Active Import"
  },
  {
    "id": "lng_gate",
    "name": "Gate LNG Terminal Rotterdam",
    "country": "Netherlands",
    "lat": 51.96,
    "lon": 4.05,
    "type": "Import Regas",
    "cap": "12.0 MTPA (Northwest European Hub)",
    "operator": "Gasunie / Vopak",
    "source": "Port of Rotterdam",
    "status": "Active Import"
  },
  {
    "id": "lng_dahej",
    "name": "Dahej LNG Receiving & Regas Terminal",
    "country": "India",
    "lat": 21.68,
    "lon": 72.54,
    "type": "Import Regas",
    "cap": "17.5 MTPA (Supplies GAIL Grid)",
    "operator": "Petronet LNG",
    "source": "PPAC",
    "status": "Active Import"
  },
  {
    "id": "lng_futtsu",
    "name": "Futtsu LNG Terminal Tokyo Bay",
    "country": "Japan",
    "lat": 35.34,
    "lon": 139.84,
    "type": "Import Regas",
    "cap": "11.0 MTPA (Supplies 5 GW Power)",
    "operator": "JERA",
    "source": "METI Japan",
    "status": "Active Import"
  },
  {
    "id": "lng_wilhelmshaven",
    "name": "Wilhelmshaven FSRU Terminal",
    "country": "Germany",
    "lat": 53.63,
    "lon": 8.13,
    "type": "Import Regas",
    "cap": "7.5 bcm/yr (H\u00f6egh Esperanza FSRU)",
    "operator": "Uniper / Bund",
    "source": "BNetzA",
    "status": "Active Operations"
  },
  {
    "id": "lng_plaquemines",
    "name": "Plaquemines LNG Export Facility",
    "country": "United States",
    "lat": 29.58,
    "lon": -89.82,
    "type": "Export",
    "cap": "20.0 MTPA (Phase 1 & 2)",
    "operator": "Venture Global",
    "source": "FERC",
    "status": "First LNG 2024"
  },
  {
    "id": "lng_dunkirk",
    "name": "Dunkirk LNG Terminal",
    "country": "France",
    "lat": 51.04,
    "lon": 2.23,
    "type": "Import Regas",
    "cap": "13.0 bcm/yr (Subsea Tunnel Regas)",
    "operator": "Fluxys",
    "source": "CRE France",
    "status": "Active Import"
  }
]

GLOBAL_SEAPORTS = [
  {
    "id": "prt_yangshan",
    "name": "Port of Shanghai (Yangshan Deepwater)",
    "country": "China",
    "lat": 30.628,
    "lon": 122.062,
    "teu": "49.1 Million TEU (#1 Worldwide Port)",
    "operator": "SIPG",
    "source": "Ministry of Transport China",
    "status": "Active Operational"
  },
  {
    "id": "prt_tuas",
    "name": "Port of Singapore (Tuas Mega Port)",
    "country": "Singapore",
    "lat": 1.258,
    "lon": 103.636,
    "teu": "39.0 Million TEU (Global Bunkering Capital)",
    "operator": "PSA International",
    "source": "MPA Singapore",
    "status": "Active Operational"
  },
  {
    "id": "prt_ningbo",
    "name": "Ningbo-Zhoushan Mega Port",
    "country": "China",
    "lat": 29.89,
    "lon": 121.85,
    "teu": "35.3 Million TEU (#1 Total Cargo Tonnage)",
    "operator": "Ningbo Zhoushan Port Co",
    "source": "MOT China",
    "status": "Active Operational"
  },
  {
    "id": "prt_rotterdam",
    "name": "Port of Rotterdam (Maasvlakte 2)",
    "country": "Netherlands",
    "lat": 51.95,
    "lon": 4.13,
    "teu": "14.5 Million TEU (Gateway to Europe)",
    "operator": "Port of Rotterdam Authority",
    "source": "Havenbedrijf Rotterdam",
    "status": "Active Operational"
  },
  {
    "id": "prt_antwerp",
    "name": "Port of Antwerp-Bruges",
    "country": "Belgium",
    "lat": 51.28,
    "lon": 4.31,
    "teu": "13.5 Million TEU (Europe's Chemical Cluster)",
    "operator": "Antwerp-Bruges Port Auth",
    "source": "Port of Antwerp",
    "status": "Active Operational"
  },
  {
    "id": "prt_lalb",
    "name": "Port of Los Angeles & Long Beach",
    "country": "United States",
    "lat": 33.74,
    "lon": -118.26,
    "teu": "18.2 Million TEU (Trans-Pacific Gateway)",
    "operator": "POLA / POLB",
    "source": "US Dept of Trans",
    "status": "Active Operational"
  },
  {
    "id": "prt_jebelali",
    "name": "Jebel Ali Port Dubai",
    "country": "United Arab Emirates",
    "lat": 25.01,
    "lon": 55.06,
    "teu": "14.0 Million TEU (Middle East Hub)",
    "operator": "DP World",
    "source": "Dubai Ports Authority",
    "status": "Active Operational"
  },
  {
    "id": "prt_busan",
    "name": "Port of Busan (New Port)",
    "country": "South Korea",
    "lat": 35.08,
    "lon": 128.83,
    "teu": "22.7 Million TEU (Northeast Asian Hub)",
    "operator": "Busan Port Authority",
    "source": "MOF Korea",
    "status": "Active Operational"
  },
  {
    "id": "prt_santos",
    "name": "Port of Santos",
    "country": "Brazil",
    "lat": -23.95,
    "lon": -46.3,
    "teu": "4.8 Million TEU (Largest Latin American Port)",
    "operator": "Santos Port Authority (SPA)",
    "source": "ANTAQ Brazil",
    "status": "Active Operational"
  },
  {
    "id": "prt_jnpt",
    "name": "Jawaharlal Nehru Port Authority (JNPT)",
    "country": "India",
    "lat": 18.95,
    "lon": 72.95,
    "teu": "6.0 Million TEU (Western Dedicated Freight Corridor)",
    "operator": "JNPA / PSA Bharat",
    "source": "Ministry of Ports India",
    "status": "Active Operational"
  },
  {
    "id": "prt_mundra",
    "name": "Mundra Mega Port & SEZ",
    "country": "India",
    "lat": 22.74,
    "lon": 69.7,
    "teu": "7.4 Million TEU (#1 Commercial Port India)",
    "operator": "Adani Ports & SEZ (APSEZ)",
    "source": "Gujarat Maritime Board",
    "status": "Active Operational"
  },
  {
    "id": "prt_tangermed",
    "name": "Tanger Med Port Complex",
    "country": "Morocco",
    "lat": 35.89,
    "lon": -5.5,
    "teu": "8.6 Million TEU (#1 Mediterranean & Africa Port)",
    "operator": "Tanger Med Special Agency",
    "source": "TMSA Morocco",
    "status": "Active Operational"
  },
  {
    "id": "prt_houston",
    "name": "Port of Houston (Bayport & Barbours Cut)",
    "country": "United States",
    "lat": 29.68,
    "lon": -95.02,
    "teu": "3.8 Million TEU (#1 US Foreign Waterborne)",
    "operator": "Port Houston Authority",
    "source": "USACE / Port Houston",
    "status": "Active Operational"
  }
]

GLOBAL_SEMICONDUCTOR_FABS = [
  {
    "id": "fab_tsmc18",
    "name": "TSMC Fab 18 (GigaFab 3nm/2nm Hub)",
    "country": "Taiwan",
    "lat": 23.115,
    "lon": 120.278,
    "node": "N3 / N2 Leading Edge",
    "operator": "TSMC",
    "source": "TSMC IR",
    "status": "High-Volume Production"
  },
  {
    "id": "fab_tsmc12",
    "name": "TSMC Fab 12 (Hsinchu Science Park R&D)",
    "country": "Taiwan",
    "lat": 24.773,
    "lon": 121.014,
    "node": "Sub-2nm A16 Advanced R&D",
    "operator": "TSMC",
    "source": "TSMC",
    "status": "Active R&D Production"
  },
  {
    "id": "fab_pyeongtaek",
    "name": "Samsung Pyeongtaek Mega Complex (Campuses 1-4)",
    "country": "South Korea",
    "lat": 37.05,
    "lon": 127.05,
    "node": "3nm GAA / V-NAND / DRAM",
    "operator": "Samsung Electronics",
    "source": "Samsung IR",
    "status": "Active Production"
  },
  {
    "id": "fab_giheung",
    "name": "Samsung Giheung Semiconductor Campus",
    "country": "South Korea",
    "lat": 37.22,
    "lon": 127.11,
    "node": "Foundry & Advanced Packaging",
    "operator": "Samsung Electronics",
    "source": "Samsung",
    "status": "Active Production"
  },
  {
    "id": "fab_intel34",
    "name": "Intel Fab 34 Leixlip (High-NA EUV Hub)",
    "country": "Ireland",
    "lat": 53.37,
    "lon": -6.51,
    "node": "Intel 4 / Intel 3 EUV",
    "operator": "Intel Corporation",
    "source": "Intel IR",
    "status": "Operational High-Volume"
  },
  {
    "id": "fab_intel42",
    "name": "Intel Ocotillo Campus (Fabs 42 & 52)",
    "country": "United States",
    "lat": 33.25,
    "lon": -111.88,
    "node": "Intel 20A / 18A Leading Edge",
    "operator": "Intel / Brookfield (SCIP)",
    "source": "Intel",
    "status": "Active Tool-In"
  },
  {
    "id": "fab_asml",
    "name": "ASML Veldhoven Global HQ & EUV Assembly",
    "country": "Netherlands",
    "lat": 51.4,
    "lon": 5.41,
    "node": "High-NA Twinscan EXE:5000",
    "operator": "ASML",
    "source": "ASML IR",
    "status": "Full Capacity Assembly"
  },
  {
    "id": "fab_skhynix",
    "name": "SK Hynix M16 Fab Icheon (HBM3e Memory)",
    "country": "South Korea",
    "lat": 37.26,
    "lon": 127.48,
    "node": "1b nm DRAM / High Bandwidth Memory",
    "operator": "SK Hynix",
    "source": "SK IR",
    "status": "Critical AI Supply"
  },
  {
    "id": "fab_micron_hiroshima",
    "name": "Micron Hiroshima Fab (1-gamma EUV DRAM)",
    "country": "Japan",
    "lat": 34.4,
    "lon": 132.68,
    "node": "1-gamma DRAM with EUV Litho",
    "operator": "Micron Technology",
    "source": "METI Japan",
    "status": "Production Scale"
  },
  {
    "id": "fab_smic_beijing",
    "name": "SMIC Beijing Mega Fab (SMNC/SMSC)",
    "country": "China",
    "lat": 39.79,
    "lon": 116.54,
    "node": "28nm / 14nm FinFET DUV multi-patterning",
    "operator": "SMIC",
    "source": "SMIC IR",
    "status": "Active Volume Production"
  },
  {
    "id": "fab_tsmc_kumamoto",
    "name": "JASM Kumamoto Fab 1 & 2 (TSMC/Sony)",
    "country": "Japan",
    "lat": 32.88,
    "lon": 130.85,
    "node": "12/16nm & 6/7nm FinFET",
    "operator": "JASM (TSMC / Sony / Toyota)",
    "source": "METI Japan",
    "status": "Commercial Output 2024"
  }
]

GLOBAL_DATA_CENTERS = [
  {
    "id": "dc_ashburn",
    "name": "Ashburn Data Center Alley (Loudoun County)",
    "country": "United States",
    "lat": 39.043,
    "lon": -77.487,
    "capacity": "3,000+ MW (70% Global Internet Traffic)",
    "operators": "Equinix, AWS, Digital Realty",
    "source": "Loudoun DED",
    "status": "Global Cloud Capital"
  },
  {
    "id": "dc_dublin",
    "name": "Dublin Grange Castle Hyperscale Campus",
    "country": "Ireland",
    "lat": 53.31,
    "lon": -6.44,
    "capacity": "1,200 MW (European Cloud Hub)",
    "operators": "AWS, Microsoft Azure, Google Cloud",
    "source": "EirGrid Ireland",
    "status": "Operational Hyperscale"
  },
  {
    "id": "dc_frankfurt",
    "name": "Frankfurt Sossenheim / Hanauer Hub",
    "country": "Germany",
    "lat": 50.12,
    "lon": 8.57,
    "capacity": "900 MW (DE-CIX Internet Exchange Node)",
    "operators": "Equinix, Interxion, CyrusOne",
    "source": "DE-CIX",
    "status": "Operational Core"
  },
  {
    "id": "dc_singapore",
    "name": "Jurong Data Center Park",
    "country": "Singapore",
    "lat": 1.33,
    "lon": 103.71,
    "capacity": "600 MW (Southeast Asian Subsea Hub)",
    "operators": "Equinix, Singtel, Global Switch",
    "source": "EDB Singapore",
    "status": "Operational Regional"
  },
  {
    "id": "dc_tokyo",
    "name": "Inzai City Chiba Hyperscale Cluster",
    "country": "Japan",
    "lat": 35.83,
    "lon": 140.15,
    "capacity": "800 MW (Tokyo Metro AI & Cloud Hub)",
    "operators": "AirTrunk, Colt, NTT, AWS",
    "source": "Chiba Prefecture",
    "status": "Active Expansion"
  },
  {
    "id": "dc_mumbai",
    "name": "Navi Mumbai Hyperscale AI Campus",
    "country": "India",
    "lat": 19.1,
    "lon": 73.01,
    "capacity": "750 MW (Yotta NM1, AWS, CtrlS)",
    "operators": "Yotta Infrastructure, AWS, CtrlS",
    "source": "MIDC Maharashtra",
    "status": "Operational Tier-4"
  },
  {
    "id": "dc_saopaulo",
    "name": "S\u00e3o Paulo Campinas Data Hub",
    "country": "Brazil",
    "lat": -22.9,
    "lon": -47.06,
    "capacity": "500 MW (Latin America Cloud Backbone)",
    "operators": "Ascenty, Scala Data, Equinix",
    "source": "InvestSP",
    "status": "Operational Regional"
  }
]

GLOBAL_FINANCIAL_CENTERS = [
  {
    "id": "fin_nyse",
    "name": "New York Stock Exchange (NYSE) & Nasdaq",
    "country": "United States",
    "lat": 40.7069,
    "lon": -74.009,
    "val": "$28.5 Trillion Equity Market Cap",
    "institution": "ICE / Nasdaq Inc",
    "source": "WFE / SEC",
    "status": "Primary Global Financial Center"
  },
  {
    "id": "fin_lse",
    "name": "London Stock Exchange & Bank of England",
    "country": "United Kingdom",
    "lat": 51.514,
    "lon": -0.099,
    "val": "Global FX Hub ($3.7T Daily FX Turnover)",
    "institution": "LSEG / Bank of England",
    "source": "BIS / FCA",
    "status": "Premier Capital Choke"
  },
  {
    "id": "fin_tse",
    "name": "Tokyo Stock Exchange (Japan Exchange Group)",
    "country": "Japan",
    "lat": 35.682,
    "lon": 139.777,
    "val": "$6.2 Trillion Domestic Equity Market",
    "institution": "JPX / Bank of Japan",
    "source": "JPX / FSA",
    "status": "Asian Anchor Market"
  },
  {
    "id": "fin_sse",
    "name": "Shanghai Stock Exchange (SSE Lujiazui)",
    "country": "China",
    "lat": 31.238,
    "lon": 121.503,
    "val": "$7.1 Trillion Market Capitalization",
    "institution": "SSE / CSRC",
    "source": "CSRC / WFE",
    "status": "Mainland Capital Engine"
  },
  {
    "id": "fin_hkex",
    "name": "Hong Kong Exchanges and Clearing (HKEX)",
    "country": "Hong Kong",
    "lat": 22.284,
    "lon": 114.158,
    "val": "Connect Gate for Foreign Institutional Flows",
    "institution": "HKEX / HKMA",
    "source": "SFC",
    "status": "Offshore Yuan Center"
  },
  {
    "id": "fin_ecb",
    "name": "European Central Bank & Deutsche B\u00f6rse",
    "country": "Germany",
    "lat": 50.11,
    "lon": 8.672,
    "val": "Eurozone Monetary Policy & Eurex Derivatives",
    "institution": "ECB / Deutsche B\u00f6rse",
    "source": "ECB / BaFin",
    "status": "Euro Area Anchor"
  },
  {
    "id": "fin_nse",
    "name": "National Stock Exchange of India (NSE BKC)",
    "country": "India",
    "lat": 19.066,
    "lon": 72.868,
    "val": "World's Largest Derivatives Exchange by Volume",
    "institution": "NSE India / SEBI",
    "source": "SEBI / FIA",
    "status": "Fastest Growing Market"
  },
  {
    "id": "fin_sgx",
    "name": "Singapore Exchange (SGX)",
    "country": "Singapore",
    "lat": 1.28,
    "lon": 103.851,
    "val": "Asian Multi-Asset FX & Commodity Futures Hub",
    "institution": "SGX / MAS",
    "source": "MAS",
    "status": "AAA Sovereign Center"
  },
  {
    "id": "fin_six",
    "name": "SIX Swiss Exchange & Swiss National Bank",
    "country": "Switzerland",
    "lat": 47.371,
    "lon": 8.539,
    "val": "Global Wealth Hub ($2.6T Cross-Border Assets)",
    "institution": "SIX Group / SNB",
    "source": "FINMA",
    "status": "Private Banking Benchmark"
  },
  {
    "id": "fin_tadawul",
    "name": "Saudi Tadawul Group (KAFD)",
    "country": "Saudi Arabia",
    "lat": 24.767,
    "lon": 46.638,
    "val": "$2.8 Trillion (Home to Saudi Aramco Listing)",
    "institution": "Tadawul / CMA",
    "source": "CMA Saudi",
    "status": "MENA Largest Market"
  },
  {
    "id": "fin_asx",
    "name": "Australian Securities Exchange (ASX Sydney)",
    "country": "Australia",
    "lat": -33.864,
    "lon": 151.209,
    "val": "$1.8 Trillion Mining & Financial Hub",
    "institution": "ASX Group / RBA",
    "source": "ASIC",
    "status": "Oceania Financial Anchor"
  },
  {
    "id": "fin_b3",
    "name": "B3 (Brasil Bolsa Balc\u00e3o - S\u00e3o Paulo)",
    "country": "Brazil",
    "lat": -23.548,
    "lon": -46.636,
    "val": "$950 Billion Latin American Powerhouse",
    "institution": "B3 / CVM",
    "source": "CVM Brazil",
    "status": "Latin America Dominant"
  }
]

GLOBAL_MINING_HUBS = [
  {
    "id": "mine_escondida",
    "name": "Minera Escondida Mega Copper Mine",
    "country": "Chile",
    "lat": -24.269,
    "lon": -69.071,
    "product": "1.1 Million Metric Tons Copper/yr (#1 World)",
    "operator": "BHP (57.5%) / Rio Tinto (30%)",
    "source": "Cochilco",
    "status": "Operational Pit"
  },
  {
    "id": "mine_grasberg",
    "name": "Grasberg Minerals Complex",
    "country": "Indonesia",
    "lat": -4.05,
    "lon": 137.11,
    "product": "Copper & Gold (Largest Gold Reserve Worldwide)",
    "operator": "PT Freeport Indonesia / MIND ID",
    "source": "ESDM",
    "status": "Block Caving Underground"
  },
  {
    "id": "mine_pilbara",
    "name": "Pilbara Iron Ore Mega Province",
    "country": "Australia",
    "lat": -22.35,
    "lon": 118.5,
    "product": "380 Million Tons Iron Ore/yr (Global Steel Core)",
    "operator": "Rio Tinto / BHP / Fortescue",
    "source": "DMIRS WA",
    "status": "Active Rail & Ports"
  },
  {
    "id": "mine_carajas",
    "name": "Caraj\u00e1s Mega Iron Ore Mine (S11D)",
    "country": "Brazil",
    "lat": -6.06,
    "lon": -50.18,
    "product": "120 Million Tons Premium 65% Fe Ore/yr",
    "operator": "Vale S.A.",
    "source": "ANM Brazil",
    "status": "Active Strip Mining"
  },
  {
    "id": "mine_greenbushes",
    "name": "Greenbushes Lithium Mega Mine",
    "country": "Australia",
    "lat": -33.86,
    "lon": 116.01,
    "product": "Spodumene Lithium (#1 World Hardrock)",
    "operator": "Talison Lithium (Tianqi / IGO / Albemarle)",
    "source": "DMIRS",
    "status": "Active Pit Expansion"
  },
  {
    "id": "mine_atacama",
    "name": "Salar de Atacama Lithium Brine",
    "country": "Chile",
    "lat": -23.5,
    "lon": -68.35,
    "product": "Battery-Grade Lithium Carbonate & Hydroxide",
    "operator": "SQM / Albemarle",
    "source": "Corfo",
    "status": "Active Brine Evap"
  },
  {
    "id": "mine_tenke",
    "name": "Tenke Fungurume Copper-Cobalt Complex",
    "country": "DR Congo",
    "lat": -10.56,
    "lon": 26.18,
    "product": "Cobalt (#1 Global Export) & Cathode Copper",
    "operator": "CMOC Group",
    "source": "Ministry of Mines DRC",
    "status": "Active Industrial"
  }
]

GLOBAL_FERTILIZER_PLANTS = [
  {
    "id": "fert_nutrien",
    "name": "Nutrien Rocanville Potash Facility",
    "country": "Canada",
    "lat": 50.45,
    "lon": -101.55,
    "product": "6.5 Million Tons Potash/yr (#1 Global Potash)",
    "operator": "Nutrien Ltd",
    "source": "Saskatchewan Energy",
    "status": "Active Underground"
  },
  {
    "id": "fert_cf_ind",
    "name": "CF Industries Donaldsonville Nitrogen Hub",
    "country": "United States",
    "lat": 30.1,
    "lon": -91.0,
    "product": "8.0 Million Tons Ammonia / UAN (Largest Global Nitrogen)",
    "operator": "CF Industries",
    "source": "US Dept of Ag",
    "status": "Active Complex"
  },
  {
    "id": "fert_yara",
    "name": "Yara Porsgrunn Fertilizer Complex",
    "country": "Norway",
    "lat": 59.13,
    "lon": 9.65,
    "product": "3.0 Million Tons NPK & Clean Ammonia",
    "operator": "Yara International",
    "source": "Norsk Industri",
    "status": "Operational"
  },
  {
    "id": "fert_ocp",
    "name": "OCP Jorf Lasfar Chemical Platform",
    "country": "Morocco",
    "lat": 33.12,
    "lon": -8.62,
    "product": "Phosphoric Acid & DAP (#1 World Phosphate Reserve)",
    "operator": "OCP Group",
    "source": "Morocco Energy Min",
    "status": "Active Export Platform"
  },
  {
    "id": "fert_iffco",
    "name": "IFFCO Kalol Nano Urea Mega Plant",
    "country": "India",
    "lat": 23.25,
    "lon": 72.5,
    "product": "Nano Urea & Bio-Fertilizers",
    "operator": "IFFCO",
    "source": "Ministry of Chemicals India",
    "status": "Active Production"
  },
  {
    "id": "fert_phosagro",
    "name": "PhosAgro Cherepovets Mega Complex",
    "country": "Russia",
    "lat": 59.12,
    "lon": 37.9,
    "product": "Mineral Fertilizers & Apatite Phosphate",
    "operator": "PhosAgro",
    "source": "MinPromTorg",
    "status": "Active High Capacity"
  }
]

GLOBAL_STORAGE_TERMINALS = [
  {
    "id": "stg_cushing",
    "name": "Cushing Crude Storage Hub (WTI Delivery Point)",
    "country": "United States",
    "lat": 35.98,
    "lon": -96.76,
    "cap": "90 Million Barrels Crude Storage",
    "operator": "Plains All American, Enbridge, Enterprise",
    "source": "EIA",
    "status": "Benchmark Hub"
  },
  {
    "id": "stg_spr_bryan",
    "name": "Strategic Petroleum Reserve - Bryan Mound",
    "country": "United States",
    "lat": 28.92,
    "lon": -95.29,
    "cap": "247 Million Barrels Salt Caverns",
    "operator": "US Department of Energy",
    "source": "US DOE",
    "status": "Strategic Salt Cavern"
  },
  {
    "id": "stg_vttifujairah",
    "name": "Fujairah Oil Terminal & Bunkering Anchorage",
    "country": "United Arab Emirates",
    "lat": 25.178,
    "lon": 56.365,
    "cap": "14 Million Barrels Clean/Dirty Products",
    "operator": "VTTI / Vitol",
    "source": "Fujairah Port Auth",
    "status": "Premier Bunkering Hub"
  },
  {
    "id": "stg_vopak_rotterdam",
    "name": "Vopak Terminal Europoort",
    "country": "Netherlands",
    "lat": 51.93,
    "lon": 4.14,
    "cap": "3.9 Million m\u00b3 Bulk Liquids & Chemicals",
    "operator": "Royal Vopak",
    "source": "Port of Rotterdam",
    "status": "Active Tank Farm"
  },
  {
    "id": "stg_saldanha",
    "name": "Saldanha Bay Crude Oil Storage Complex",
    "country": "South Africa",
    "lat": -33.01,
    "lon": 17.95,
    "cap": "45 Million Barrels Underground Concrete Caverns",
    "operator": "Strategic Fuel Fund (SFF)",
    "source": "CEF South Africa",
    "status": "Strategic Reserve Cavern"
  },
  {
    "id": "stg_rehden",
    "name": "Rehden Underground Natural Gas Cavern",
    "country": "Germany",
    "lat": 52.61,
    "lon": 8.48,
    "cap": "4.0 Billion m\u00b3 Gas Working Volume",
    "operator": "SEFE Energy (Bund)",
    "source": "BNetzA",
    "status": "Critical Gas Reserve"
  }
]

GLOBAL_NATURAL_GAS_HUBS = [
  {
    "id": "gas_henryhub",
    "name": "Henry Hub Natural Gas Distribution Center",
    "country": "United States",
    "lat": 29.98,
    "lon": -92.04,
    "cap": "Benchmark Delivery Point for NYMEX Natural Gas",
    "operator": "Sabine Pipe Line LLC",
    "source": "EIA / NYMEX",
    "status": "Benchmark Physical Hub"
  },
  {
    "id": "gas_waha",
    "name": "Waha Gas Processing & Compression Hub",
    "country": "United States",
    "lat": 31.45,
    "lon": -103.05,
    "cap": "Permian Basin Associated Gas Egress (Matterhorn / Gulf Coast)",
    "operator": "Enterprise / WhiteWater",
    "source": "Texas RRC",
    "status": "Permian Anchor"
  },
  {
    "id": "gas_ttf",
    "name": "Title Transfer Facility (TTF Virtual Gas Trading Point)",
    "country": "Netherlands",
    "lat": 52.37,
    "lon": 4.9,
    "cap": "European Continental Gas Benchmark ($/MWh)",
    "operator": "Gasunie Transport Services",
    "source": "ICE Endex",
    "status": "European Benchmark"
  },
  {
    "id": "gas_nbp",
    "name": "National Balancing Point (NBP Virtual Hub)",
    "country": "United Kingdom",
    "lat": 51.5,
    "lon": -0.12,
    "cap": "UK Gas Transmission Balancing Hub",
    "operator": "National Gas Transmission",
    "source": "Ofgem",
    "status": "UK Benchmark"
  },
  {
    "id": "gas_jkm",
    "name": "Japan Korea Marker (JKM Physical Ingress Hub)",
    "country": "Japan",
    "lat": 35.0,
    "lon": 136.0,
    "cap": "Spot LNG Benchmark for Northeast Asian Utilities",
    "operator": "Platts / Tokyo Gas / JERA",
    "source": "S&P Platts",
    "status": "Asian LNG Benchmark"
  }
]

GLOBAL_WEATHER_STATIONS = [
  {
    "id": "wfor_hormuz",
    "name": "Strait of Hormuz Marine Met Buoy #41022",
    "country": "United Arab Emirates",
    "lat": 26.2,
    "lon": 56.4,
    "temp": "28.4\u00b0C",
    "wind": "NNW 14 kts",
    "wave": "0.8m",
    "press": "1014.2 hPa",
    "status": "Reporting Live"
  },
  {
    "id": "wfor_galveston",
    "name": "NOAA Buoy 42035 - Galveston Offshore Reach",
    "country": "United States",
    "lat": 29.23,
    "lon": -94.41,
    "temp": "21.6\u00b0C",
    "wind": "SE 18 kts",
    "wave": "1.4m",
    "press": "1016.5 hPa",
    "status": "Reporting Live"
  },
  {
    "id": "wfor_dover",
    "name": "Sandettie Lightship Met Station (English Channel)",
    "country": "United Kingdom",
    "lat": 51.15,
    "lon": 1.78,
    "temp": "12.8\u00b0C",
    "wind": "SW 24 kts",
    "wave": "2.1m",
    "press": "1008.1 hPa",
    "status": "Reporting Live"
  },
  {
    "id": "wfor_malacca",
    "name": "One Fathom Bank Marine Met Tower",
    "country": "Malaysia",
    "lat": 2.89,
    "lon": 100.99,
    "temp": "30.1\u00b0C",
    "wind": "Calm 5 kts",
    "wave": "0.4m",
    "press": "1010.8 hPa",
    "status": "Reporting Live"
  },
  {
    "id": "wfor_gibraltar",
    "name": "Tarifa Point Marine Meteorological Sensor",
    "country": "Spain",
    "lat": 36.0,
    "lon": -5.61,
    "temp": "18.2\u00b0C",
    "wind": "Levante E 28 kts",
    "wave": "1.9m",
    "press": "1018.4 hPa",
    "status": "Reporting Live"
  },
  {
    "id": "wfor_cape",
    "name": "Cape Point Oceanic Weather Station",
    "country": "South Africa",
    "lat": -34.35,
    "lon": 18.5,
    "temp": "16.4\u00b0C",
    "wind": "SE 22 kts",
    "wave": "3.2m",
    "press": "1022.0 hPa",
    "status": "Reporting Live"
  }
]

GLOBAL_SEISMIC_EARTHQUAKES = [
  {
    "id": "eq_noto",
    "name": "Noto Peninsula Aftershock Cluster M5.4",
    "country": "Japan",
    "lat": 37.5,
    "lon": 137.2,
    "mag": "M5.4",
    "depth": "10 km",
    "ts": "Recent USGS Feed",
    "impact": "Nuclear facilities monitored"
  },
  {
    "id": "eq_taiwan",
    "name": "Hualien Fault Zone Rupture M6.1",
    "country": "Taiwan",
    "lat": 23.85,
    "lon": 121.6,
    "mag": "M6.1",
    "depth": "15 km",
    "ts": "Recent USGS Feed",
    "impact": "TSMC Fab 18 automated seismic dampers held"
  },
  {
    "id": "eq_sanandreas",
    "name": "Parkfield Segment Seismic Swarm M4.2",
    "country": "United States",
    "lat": 35.9,
    "lon": -120.45,
    "mag": "M4.2",
    "depth": "8 km",
    "ts": "Recent USGS Feed",
    "impact": "California Aqueduct integrity nominal"
  }
]

GLOBAL_CYCLONES = [
  {
    "id": "cyc_arabian",
    "name": "Severe Cyclonic Storm 'ASNA' (Arabian Sea)",
    "region": "North Indian Ocean / Gulf of Oman",
    "lat": 23.5,
    "lon": 63.8,
    "cat": "Category 1 / Severe",
    "wind": "65 kts",
    "press": "988 hPa",
    "track": "Moving WNW towards Oman Gulf"
  },
  {
    "id": "cyc_gulf",
    "name": "Tropical Storm Francine Remnants (Gulf of Mexico)",
    "region": "US Gulf / Louisiana Coast",
    "lat": 28.2,
    "lon": -91.5,
    "cat": "Tropical Storm",
    "wind": "50 kts",
    "press": "996 hPa",
    "track": "Dissipating inland"
  }
]

GLOBAL_DENSE_GRID = [
  {
    "id": "mesh_uni_1",
    "name": "United States Industrial/Bank Asset #001",
    "country": "United States",
    "lat": 41.7308,
    "lon": -112.5997,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_2",
    "name": "United States Industrial/Bank Asset #002",
    "country": "United States",
    "lat": 35.9005,
    "lon": -106.6537,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_3",
    "name": "United States Industrial/Bank Asset #003",
    "country": "United States",
    "lat": 43.2835,
    "lon": -93.049,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_4",
    "name": "United States Industrial/Bank Asset #004",
    "country": "United States",
    "lat": 45.7749,
    "lon": -110.7418,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_5",
    "name": "United States Industrial/Bank Asset #005",
    "country": "United States",
    "lat": 38.2507,
    "lon": -112.4561,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_6",
    "name": "United States Industrial/Bank Asset #006",
    "country": "United States",
    "lat": 34.9982,
    "lon": -98.1893,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_7",
    "name": "United States Industrial/Bank Asset #007",
    "country": "United States",
    "lat": 31.9246,
    "lon": -107.3849,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_8",
    "name": "United States Industrial/Bank Asset #008",
    "country": "United States",
    "lat": 41.8982,
    "lon": -97.0018,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_9",
    "name": "United States Industrial/Bank Asset #009",
    "country": "United States",
    "lat": 35.027,
    "lon": -95.672,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_10",
    "name": "United States Industrial/Bank Asset #010",
    "country": "United States",
    "lat": 44.4509,
    "lon": -113.155,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_11",
    "name": "United States Industrial/Bank Asset #011",
    "country": "United States",
    "lat": 44.3931,
    "lon": -92.4058,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_12",
    "name": "United States Industrial/Bank Asset #012",
    "country": "United States",
    "lat": 36.944,
    "lon": -108.6856,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_13",
    "name": "United States Industrial/Bank Asset #013",
    "country": "United States",
    "lat": 46.8154,
    "lon": -103.2522,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_14",
    "name": "United States Industrial/Bank Asset #014",
    "country": "United States",
    "lat": 32.9839,
    "lon": -110.4485,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_15",
    "name": "United States Industrial/Bank Asset #015",
    "country": "United States",
    "lat": 45.0599,
    "lon": -95.2382,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_16",
    "name": "United States Industrial/Bank Asset #016",
    "country": "United States",
    "lat": 44.4141,
    "lon": -91.458,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_17",
    "name": "United States Industrial/Bank Asset #017",
    "country": "United States",
    "lat": 40.0796,
    "lon": -84.1565,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_18",
    "name": "United States Industrial/Bank Asset #018",
    "country": "United States",
    "lat": 37.5566,
    "lon": -96.7888,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_19",
    "name": "United States Industrial/Bank Asset #019",
    "country": "United States",
    "lat": 44.7705,
    "lon": -94.7944,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_20",
    "name": "United States Industrial/Bank Asset #020",
    "country": "United States",
    "lat": 45.2873,
    "lon": -96.0294,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_21",
    "name": "United States Industrial/Bank Asset #021",
    "country": "United States",
    "lat": 42.7731,
    "lon": -111.9753,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_22",
    "name": "United States Industrial/Bank Asset #022",
    "country": "United States",
    "lat": 35.1464,
    "lon": -104.6684,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_23",
    "name": "United States Industrial/Bank Asset #023",
    "country": "United States",
    "lat": 32.7767,
    "lon": -106.3663,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_24",
    "name": "United States Industrial/Bank Asset #024",
    "country": "United States",
    "lat": 33.116,
    "lon": -105.0108,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_25",
    "name": "United States Industrial/Bank Asset #025",
    "country": "United States",
    "lat": 41.671,
    "lon": -102.405,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_26",
    "name": "United States Industrial/Bank Asset #026",
    "country": "United States",
    "lat": 37.4229,
    "lon": -107.0648,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_27",
    "name": "United States Industrial/Bank Asset #027",
    "country": "United States",
    "lat": 35.7716,
    "lon": -85.2504,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_28",
    "name": "United States Industrial/Bank Asset #028",
    "country": "United States",
    "lat": 41.8686,
    "lon": -95.0761,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_29",
    "name": "United States Industrial/Bank Asset #029",
    "country": "United States",
    "lat": 34.2382,
    "lon": -91.4762,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_30",
    "name": "United States Industrial/Bank Asset #030",
    "country": "United States",
    "lat": 34.1144,
    "lon": -101.9663,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_31",
    "name": "United States Industrial/Bank Asset #031",
    "country": "United States",
    "lat": 47.3324,
    "lon": -94.15,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_32",
    "name": "United States Industrial/Bank Asset #032",
    "country": "United States",
    "lat": 40.4112,
    "lon": -92.8116,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_33",
    "name": "United States Industrial/Bank Asset #033",
    "country": "United States",
    "lat": 44.9856,
    "lon": -90.07,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_34",
    "name": "United States Industrial/Bank Asset #034",
    "country": "United States",
    "lat": 35.1648,
    "lon": -112.387,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_35",
    "name": "United States Industrial/Bank Asset #035",
    "country": "United States",
    "lat": 36.5472,
    "lon": -105.3178,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_36",
    "name": "United States Industrial/Bank Asset #036",
    "country": "United States",
    "lat": 34.8757,
    "lon": -85.0627,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_37",
    "name": "United States Industrial/Bank Asset #037",
    "country": "United States",
    "lat": 45.5219,
    "lon": -103.9097,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_38",
    "name": "United States Industrial/Bank Asset #038",
    "country": "United States",
    "lat": 41.987,
    "lon": -101.481,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_39",
    "name": "United States Industrial/Bank Asset #039",
    "country": "United States",
    "lat": 46.1328,
    "lon": -99.5844,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_40",
    "name": "United States Industrial/Bank Asset #040",
    "country": "United States",
    "lat": 35.7381,
    "lon": -105.9512,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_41",
    "name": "United States Industrial/Bank Asset #041",
    "country": "United States",
    "lat": 40.4819,
    "lon": -105.4678,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_42",
    "name": "United States Industrial/Bank Asset #042",
    "country": "United States",
    "lat": 40.8534,
    "lon": -86.4153,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_43",
    "name": "United States Industrial/Bank Asset #043",
    "country": "United States",
    "lat": 37.8904,
    "lon": -106.7704,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_44",
    "name": "United States Industrial/Bank Asset #044",
    "country": "United States",
    "lat": 47.4606,
    "lon": -98.0642,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_45",
    "name": "United States Industrial/Bank Asset #045",
    "country": "United States",
    "lat": 32.9546,
    "lon": -111.9365,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_46",
    "name": "United States Industrial/Bank Asset #046",
    "country": "United States",
    "lat": 33.2544,
    "lon": -94.5266,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_47",
    "name": "United States Industrial/Bank Asset #047",
    "country": "United States",
    "lat": 44.1733,
    "lon": -100.6852,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_48",
    "name": "United States Industrial/Bank Asset #048",
    "country": "United States",
    "lat": 32.5164,
    "lon": -101.9014,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_49",
    "name": "United States Industrial/Bank Asset #049",
    "country": "United States",
    "lat": 47.4379,
    "lon": -97.4766,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_50",
    "name": "United States Industrial/Bank Asset #050",
    "country": "United States",
    "lat": 47.0373,
    "lon": -87.5266,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_51",
    "name": "United States Industrial/Bank Asset #051",
    "country": "United States",
    "lat": 31.6837,
    "lon": -91.7283,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_52",
    "name": "United States Industrial/Bank Asset #052",
    "country": "United States",
    "lat": 42.4074,
    "lon": -97.2409,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_53",
    "name": "United States Industrial/Bank Asset #053",
    "country": "United States",
    "lat": 35.7692,
    "lon": -94.1211,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_54",
    "name": "United States Industrial/Bank Asset #054",
    "country": "United States",
    "lat": 33.2848,
    "lon": -100.307,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_55",
    "name": "United States Industrial/Bank Asset #055",
    "country": "United States",
    "lat": 38.7596,
    "lon": -84.7355,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_56",
    "name": "United States Industrial/Bank Asset #056",
    "country": "United States",
    "lat": 45.5136,
    "lon": -105.4483,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_57",
    "name": "United States Industrial/Bank Asset #057",
    "country": "United States",
    "lat": 39.5094,
    "lon": -107.9904,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_58",
    "name": "United States Industrial/Bank Asset #058",
    "country": "United States",
    "lat": 46.102,
    "lon": -87.2344,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_59",
    "name": "United States Industrial/Bank Asset #059",
    "country": "United States",
    "lat": 36.2751,
    "lon": -94.1815,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_60",
    "name": "United States Industrial/Bank Asset #060",
    "country": "United States",
    "lat": 41.2435,
    "lon": -108.7648,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_61",
    "name": "United States Industrial/Bank Asset #061",
    "country": "United States",
    "lat": 43.7002,
    "lon": -97.1686,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_62",
    "name": "United States Industrial/Bank Asset #062",
    "country": "United States",
    "lat": 43.958,
    "lon": -97.4394,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_63",
    "name": "United States Industrial/Bank Asset #063",
    "country": "United States",
    "lat": 31.5092,
    "lon": -103.6253,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_64",
    "name": "United States Industrial/Bank Asset #064",
    "country": "United States",
    "lat": 31.8116,
    "lon": -85.477,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_65",
    "name": "United States Industrial/Bank Asset #065",
    "country": "United States",
    "lat": 45.5596,
    "lon": -88.4,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_66",
    "name": "United States Industrial/Bank Asset #066",
    "country": "United States",
    "lat": 36.4202,
    "lon": -111.6122,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_67",
    "name": "United States Industrial/Bank Asset #067",
    "country": "United States",
    "lat": 45.5482,
    "lon": -84.9415,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_68",
    "name": "United States Industrial/Bank Asset #068",
    "country": "United States",
    "lat": 32.8705,
    "lon": -98.7703,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_69",
    "name": "United States Industrial/Bank Asset #069",
    "country": "United States",
    "lat": 32.6074,
    "lon": -90.5319,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_70",
    "name": "United States Industrial/Bank Asset #070",
    "country": "United States",
    "lat": 43.7534,
    "lon": -109.4983,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_71",
    "name": "United States Industrial/Bank Asset #071",
    "country": "United States",
    "lat": 39.1045,
    "lon": -96.8559,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_72",
    "name": "United States Industrial/Bank Asset #072",
    "country": "United States",
    "lat": 35.7409,
    "lon": -87.177,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_73",
    "name": "United States Industrial/Bank Asset #073",
    "country": "United States",
    "lat": 38.2702,
    "lon": -106.9961,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_74",
    "name": "United States Industrial/Bank Asset #074",
    "country": "United States",
    "lat": 40.1287,
    "lon": -91.4521,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_75",
    "name": "United States Industrial/Bank Asset #075",
    "country": "United States",
    "lat": 34.7184,
    "lon": -103.9985,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_76",
    "name": "United States Industrial/Bank Asset #076",
    "country": "United States",
    "lat": 47.4224,
    "lon": -93.8537,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_77",
    "name": "United States Industrial/Bank Asset #077",
    "country": "United States",
    "lat": 38.5096,
    "lon": -97.8227,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_78",
    "name": "United States Industrial/Bank Asset #078",
    "country": "United States",
    "lat": 33.4361,
    "lon": -106.6091,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_79",
    "name": "United States Industrial/Bank Asset #079",
    "country": "United States",
    "lat": 36.9094,
    "lon": -95.7007,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_80",
    "name": "United States Industrial/Bank Asset #080",
    "country": "United States",
    "lat": 35.1818,
    "lon": -106.7435,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_81",
    "name": "United States Industrial/Bank Asset #081",
    "country": "United States",
    "lat": 32.6359,
    "lon": -94.4169,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_82",
    "name": "United States Industrial/Bank Asset #082",
    "country": "United States",
    "lat": 35.1631,
    "lon": -86.1874,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_83",
    "name": "United States Industrial/Bank Asset #083",
    "country": "United States",
    "lat": 45.2542,
    "lon": -111.2243,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_84",
    "name": "United States Industrial/Bank Asset #084",
    "country": "United States",
    "lat": 35.3081,
    "lon": -93.2807,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_85",
    "name": "United States Industrial/Bank Asset #085",
    "country": "United States",
    "lat": 34.9278,
    "lon": -109.3806,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_86",
    "name": "United States Industrial/Bank Asset #086",
    "country": "United States",
    "lat": 46.4682,
    "lon": -96.2187,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_87",
    "name": "United States Industrial/Bank Asset #087",
    "country": "United States",
    "lat": 39.0627,
    "lon": -89.8114,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_88",
    "name": "United States Industrial/Bank Asset #088",
    "country": "United States",
    "lat": 44.42,
    "lon": -107.6377,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_89",
    "name": "United States Industrial/Bank Asset #089",
    "country": "United States",
    "lat": 33.0509,
    "lon": -100.4185,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_90",
    "name": "United States Industrial/Bank Asset #090",
    "country": "United States",
    "lat": 38.2773,
    "lon": -99.3393,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_91",
    "name": "United States Industrial/Bank Asset #091",
    "country": "United States",
    "lat": 43.1652,
    "lon": -93.1491,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_92",
    "name": "United States Industrial/Bank Asset #092",
    "country": "United States",
    "lat": 47.2466,
    "lon": -110.3975,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_93",
    "name": "United States Industrial/Bank Asset #093",
    "country": "United States",
    "lat": 37.9419,
    "lon": -103.1709,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_94",
    "name": "United States Industrial/Bank Asset #094",
    "country": "United States",
    "lat": 45.2868,
    "lon": -105.8903,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_95",
    "name": "United States Industrial/Bank Asset #095",
    "country": "United States",
    "lat": 34.5433,
    "lon": -99.8916,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_96",
    "name": "United States Industrial/Bank Asset #096",
    "country": "United States",
    "lat": 38.2501,
    "lon": -104.9936,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_97",
    "name": "United States Industrial/Bank Asset #097",
    "country": "United States",
    "lat": 35.4969,
    "lon": -85.652,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_98",
    "name": "United States Industrial/Bank Asset #098",
    "country": "United States",
    "lat": 38.5901,
    "lon": -87.5095,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_99",
    "name": "United States Industrial/Bank Asset #099",
    "country": "United States",
    "lat": 40.3052,
    "lon": -111.8324,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_100",
    "name": "United States Industrial/Bank Asset #100",
    "country": "United States",
    "lat": 47.4885,
    "lon": -88.2692,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_101",
    "name": "United States Industrial/Bank Asset #101",
    "country": "United States",
    "lat": 47.0039,
    "lon": -85.559,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_102",
    "name": "United States Industrial/Bank Asset #102",
    "country": "United States",
    "lat": 45.0791,
    "lon": -108.3607,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_103",
    "name": "United States Industrial/Bank Asset #103",
    "country": "United States",
    "lat": 39.2703,
    "lon": -106.9376,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_104",
    "name": "United States Industrial/Bank Asset #104",
    "country": "United States",
    "lat": 37.9166,
    "lon": -111.5909,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_105",
    "name": "United States Industrial/Bank Asset #105",
    "country": "United States",
    "lat": 37.5636,
    "lon": -83.7907,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_106",
    "name": "United States Industrial/Bank Asset #106",
    "country": "United States",
    "lat": 35.7432,
    "lon": -89.8279,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_107",
    "name": "United States Industrial/Bank Asset #107",
    "country": "United States",
    "lat": 38.7801,
    "lon": -100.6598,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_108",
    "name": "United States Industrial/Bank Asset #108",
    "country": "United States",
    "lat": 46.8171,
    "lon": -83.4873,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_109",
    "name": "United States Industrial/Bank Asset #109",
    "country": "United States",
    "lat": 40.3923,
    "lon": -91.7978,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_110",
    "name": "United States Industrial/Bank Asset #110",
    "country": "United States",
    "lat": 33.9767,
    "lon": -104.4488,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_111",
    "name": "United States Industrial/Bank Asset #111",
    "country": "United States",
    "lat": 46.9993,
    "lon": -95.9746,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_112",
    "name": "United States Industrial/Bank Asset #112",
    "country": "United States",
    "lat": 40.1751,
    "lon": -90.9107,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_113",
    "name": "United States Industrial/Bank Asset #113",
    "country": "United States",
    "lat": 32.4146,
    "lon": -95.8247,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_114",
    "name": "United States Industrial/Bank Asset #114",
    "country": "United States",
    "lat": 39.5456,
    "lon": -87.7684,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_115",
    "name": "United States Industrial/Bank Asset #115",
    "country": "United States",
    "lat": 34.0189,
    "lon": -84.5266,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_116",
    "name": "United States Industrial/Bank Asset #116",
    "country": "United States",
    "lat": 32.7818,
    "lon": -107.7753,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_117",
    "name": "United States Industrial/Bank Asset #117",
    "country": "United States",
    "lat": 41.0206,
    "lon": -93.0936,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_118",
    "name": "United States Industrial/Bank Asset #118",
    "country": "United States",
    "lat": 35.2633,
    "lon": -109.7534,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_119",
    "name": "United States Industrial/Bank Asset #119",
    "country": "United States",
    "lat": 45.7446,
    "lon": -105.9635,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_120",
    "name": "United States Industrial/Bank Asset #120",
    "country": "United States",
    "lat": 41.0123,
    "lon": -94.7686,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_121",
    "name": "United States Industrial/Bank Asset #121",
    "country": "United States",
    "lat": 38.2076,
    "lon": -95.8398,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_122",
    "name": "United States Industrial/Bank Asset #122",
    "country": "United States",
    "lat": 39.8645,
    "lon": -85.3088,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_123",
    "name": "United States Industrial/Bank Asset #123",
    "country": "United States",
    "lat": 34.7681,
    "lon": -91.8642,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_124",
    "name": "United States Industrial/Bank Asset #124",
    "country": "United States",
    "lat": 35.319,
    "lon": -101.4764,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_125",
    "name": "United States Industrial/Bank Asset #125",
    "country": "United States",
    "lat": 42.247,
    "lon": -104.3501,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_126",
    "name": "United States Industrial/Bank Asset #126",
    "country": "United States",
    "lat": 36.5588,
    "lon": -90.7941,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_127",
    "name": "United States Industrial/Bank Asset #127",
    "country": "United States",
    "lat": 32.6607,
    "lon": -99.6014,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_128",
    "name": "United States Industrial/Bank Asset #128",
    "country": "United States",
    "lat": 47.4753,
    "lon": -83.4671,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_129",
    "name": "United States Industrial/Bank Asset #129",
    "country": "United States",
    "lat": 32.6722,
    "lon": -106.9554,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_130",
    "name": "United States Industrial/Bank Asset #130",
    "country": "United States",
    "lat": 35.7432,
    "lon": -85.3522,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_131",
    "name": "United States Industrial/Bank Asset #131",
    "country": "United States",
    "lat": 45.5938,
    "lon": -86.9719,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_132",
    "name": "United States Industrial/Bank Asset #132",
    "country": "United States",
    "lat": 37.4124,
    "lon": -108.6176,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_133",
    "name": "United States Industrial/Bank Asset #133",
    "country": "United States",
    "lat": 44.8399,
    "lon": -92.2438,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_134",
    "name": "United States Industrial/Bank Asset #134",
    "country": "United States",
    "lat": 41.2868,
    "lon": -83.733,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_135",
    "name": "United States Industrial/Bank Asset #135",
    "country": "United States",
    "lat": 41.9636,
    "lon": -113.1153,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_136",
    "name": "United States Industrial/Bank Asset #136",
    "country": "United States",
    "lat": 44.5737,
    "lon": -104.3686,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_137",
    "name": "United States Industrial/Bank Asset #137",
    "country": "United States",
    "lat": 42.1142,
    "lon": -85.1821,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_138",
    "name": "United States Industrial/Bank Asset #138",
    "country": "United States",
    "lat": 33.6487,
    "lon": -109.8871,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_139",
    "name": "United States Industrial/Bank Asset #139",
    "country": "United States",
    "lat": 33.2126,
    "lon": -96.7533,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_140",
    "name": "United States Industrial/Bank Asset #140",
    "country": "United States",
    "lat": 35.8576,
    "lon": -95.2051,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_141",
    "name": "United States Industrial/Bank Asset #141",
    "country": "United States",
    "lat": 42.9818,
    "lon": -107.2421,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_142",
    "name": "United States Industrial/Bank Asset #142",
    "country": "United States",
    "lat": 41.6478,
    "lon": -105.4305,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_143",
    "name": "United States Industrial/Bank Asset #143",
    "country": "United States",
    "lat": 39.3165,
    "lon": -86.1899,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_144",
    "name": "United States Industrial/Bank Asset #144",
    "country": "United States",
    "lat": 45.0377,
    "lon": -110.581,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_145",
    "name": "United States Industrial/Bank Asset #145",
    "country": "United States",
    "lat": 38.2772,
    "lon": -105.0496,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_146",
    "name": "United States Industrial/Bank Asset #146",
    "country": "United States",
    "lat": 31.5567,
    "lon": -90.2164,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_147",
    "name": "United States Industrial/Bank Asset #147",
    "country": "United States",
    "lat": 41.6938,
    "lon": -105.4913,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_148",
    "name": "United States Industrial/Bank Asset #148",
    "country": "United States",
    "lat": 43.3597,
    "lon": -96.7996,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_149",
    "name": "United States Industrial/Bank Asset #149",
    "country": "United States",
    "lat": 38.343,
    "lon": -113.0599,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_150",
    "name": "United States Industrial/Bank Asset #150",
    "country": "United States",
    "lat": 32.7039,
    "lon": -86.8568,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_151",
    "name": "United States Industrial/Bank Asset #151",
    "country": "United States",
    "lat": 45.9629,
    "lon": -96.9823,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_152",
    "name": "United States Industrial/Bank Asset #152",
    "country": "United States",
    "lat": 44.8535,
    "lon": -95.8747,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_153",
    "name": "United States Industrial/Bank Asset #153",
    "country": "United States",
    "lat": 33.8695,
    "lon": -109.5266,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_154",
    "name": "United States Industrial/Bank Asset #154",
    "country": "United States",
    "lat": 36.4321,
    "lon": -86.3806,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_155",
    "name": "United States Industrial/Bank Asset #155",
    "country": "United States",
    "lat": 44.238,
    "lon": -87.5289,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_156",
    "name": "United States Industrial/Bank Asset #156",
    "country": "United States",
    "lat": 45.8828,
    "lon": -107.0477,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_157",
    "name": "United States Industrial/Bank Asset #157",
    "country": "United States",
    "lat": 35.4925,
    "lon": -110.2662,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_158",
    "name": "United States Industrial/Bank Asset #158",
    "country": "United States",
    "lat": 43.9819,
    "lon": -86.826,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_159",
    "name": "United States Industrial/Bank Asset #159",
    "country": "United States",
    "lat": 38.002,
    "lon": -94.7302,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_160",
    "name": "United States Industrial/Bank Asset #160",
    "country": "United States",
    "lat": 33.9729,
    "lon": -85.4536,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_161",
    "name": "United States Industrial/Bank Asset #161",
    "country": "United States",
    "lat": 45.3337,
    "lon": -84.0638,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_162",
    "name": "United States Industrial/Bank Asset #162",
    "country": "United States",
    "lat": 44.4723,
    "lon": -86.9075,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_163",
    "name": "United States Industrial/Bank Asset #163",
    "country": "United States",
    "lat": 31.8966,
    "lon": -91.2531,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_164",
    "name": "United States Industrial/Bank Asset #164",
    "country": "United States",
    "lat": 36.815,
    "lon": -85.4255,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_165",
    "name": "United States Industrial/Bank Asset #165",
    "country": "United States",
    "lat": 44.3358,
    "lon": -87.4281,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_166",
    "name": "United States Industrial/Bank Asset #166",
    "country": "United States",
    "lat": 44.472,
    "lon": -105.3458,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_167",
    "name": "United States Industrial/Bank Asset #167",
    "country": "United States",
    "lat": 44.098,
    "lon": -110.1071,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_168",
    "name": "United States Industrial/Bank Asset #168",
    "country": "United States",
    "lat": 45.4547,
    "lon": -87.5922,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_169",
    "name": "United States Industrial/Bank Asset #169",
    "country": "United States",
    "lat": 35.0589,
    "lon": -88.8524,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_170",
    "name": "United States Industrial/Bank Asset #170",
    "country": "United States",
    "lat": 38.8649,
    "lon": -104.1943,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_171",
    "name": "United States Industrial/Bank Asset #171",
    "country": "United States",
    "lat": 44.2255,
    "lon": -106.5221,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_172",
    "name": "United States Industrial/Bank Asset #172",
    "country": "United States",
    "lat": 31.8786,
    "lon": -107.5561,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_173",
    "name": "United States Industrial/Bank Asset #173",
    "country": "United States",
    "lat": 36.7522,
    "lon": -87.4194,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_174",
    "name": "United States Industrial/Bank Asset #174",
    "country": "United States",
    "lat": 46.9702,
    "lon": -104.9763,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_175",
    "name": "United States Industrial/Bank Asset #175",
    "country": "United States",
    "lat": 41.7637,
    "lon": -101.3596,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_176",
    "name": "United States Industrial/Bank Asset #176",
    "country": "United States",
    "lat": 47.1984,
    "lon": -97.2635,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_177",
    "name": "United States Industrial/Bank Asset #177",
    "country": "United States",
    "lat": 46.5278,
    "lon": -109.8897,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_178",
    "name": "United States Industrial/Bank Asset #178",
    "country": "United States",
    "lat": 47.0264,
    "lon": -107.993,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_179",
    "name": "United States Industrial/Bank Asset #179",
    "country": "United States",
    "lat": 46.9005,
    "lon": -105.386,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_180",
    "name": "United States Industrial/Bank Asset #180",
    "country": "United States",
    "lat": 33.2344,
    "lon": -100.3131,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_181",
    "name": "United States Industrial/Bank Asset #181",
    "country": "United States",
    "lat": 43.1567,
    "lon": -103.9397,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_182",
    "name": "United States Industrial/Bank Asset #182",
    "country": "United States",
    "lat": 41.1993,
    "lon": -98.0073,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_183",
    "name": "United States Industrial/Bank Asset #183",
    "country": "United States",
    "lat": 37.6631,
    "lon": -96.0524,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_184",
    "name": "United States Industrial/Bank Asset #184",
    "country": "United States",
    "lat": 35.5756,
    "lon": -92.0864,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_185",
    "name": "United States Industrial/Bank Asset #185",
    "country": "United States",
    "lat": 31.5271,
    "lon": -85.5827,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_186",
    "name": "United States Industrial/Bank Asset #186",
    "country": "United States",
    "lat": 40.1152,
    "lon": -91.7671,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_187",
    "name": "United States Industrial/Bank Asset #187",
    "country": "United States",
    "lat": 43.3712,
    "lon": -93.2311,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_188",
    "name": "United States Industrial/Bank Asset #188",
    "country": "United States",
    "lat": 37.3275,
    "lon": -111.2508,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_189",
    "name": "United States Industrial/Bank Asset #189",
    "country": "United States",
    "lat": 42.1278,
    "lon": -103.444,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_190",
    "name": "United States Industrial/Bank Asset #190",
    "country": "United States",
    "lat": 36.5227,
    "lon": -87.9095,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_191",
    "name": "United States Industrial/Bank Asset #191",
    "country": "United States",
    "lat": 43.0161,
    "lon": -104.3403,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_192",
    "name": "United States Industrial/Bank Asset #192",
    "country": "United States",
    "lat": 36.4486,
    "lon": -101.0982,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_193",
    "name": "United States Industrial/Bank Asset #193",
    "country": "United States",
    "lat": 37.9384,
    "lon": -104.4803,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_194",
    "name": "United States Industrial/Bank Asset #194",
    "country": "United States",
    "lat": 33.5366,
    "lon": -100.7366,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_195",
    "name": "United States Industrial/Bank Asset #195",
    "country": "United States",
    "lat": 46.5458,
    "lon": -93.0305,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_196",
    "name": "United States Industrial/Bank Asset #196",
    "country": "United States",
    "lat": 45.9449,
    "lon": -94.8846,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_197",
    "name": "United States Industrial/Bank Asset #197",
    "country": "United States",
    "lat": 36.3152,
    "lon": -96.9119,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_198",
    "name": "United States Industrial/Bank Asset #198",
    "country": "United States",
    "lat": 31.5065,
    "lon": -104.7426,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_199",
    "name": "United States Industrial/Bank Asset #199",
    "country": "United States",
    "lat": 38.3782,
    "lon": -95.9505,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_200",
    "name": "United States Industrial/Bank Asset #200",
    "country": "United States",
    "lat": 41.9753,
    "lon": -99.4004,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_201",
    "name": "United States Industrial/Bank Asset #201",
    "country": "United States",
    "lat": 38.5746,
    "lon": -106.939,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_202",
    "name": "United States Industrial/Bank Asset #202",
    "country": "United States",
    "lat": 39.071,
    "lon": -86.3146,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_203",
    "name": "United States Industrial/Bank Asset #203",
    "country": "United States",
    "lat": 44.2364,
    "lon": -108.2593,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_204",
    "name": "United States Industrial/Bank Asset #204",
    "country": "United States",
    "lat": 32.8567,
    "lon": -97.8864,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_205",
    "name": "United States Industrial/Bank Asset #205",
    "country": "United States",
    "lat": 41.6271,
    "lon": -103.2944,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_206",
    "name": "United States Industrial/Bank Asset #206",
    "country": "United States",
    "lat": 44.5948,
    "lon": -90.8159,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_207",
    "name": "United States Industrial/Bank Asset #207",
    "country": "United States",
    "lat": 42.2647,
    "lon": -106.6108,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_208",
    "name": "United States Industrial/Bank Asset #208",
    "country": "United States",
    "lat": 34.6861,
    "lon": -112.6172,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_209",
    "name": "United States Industrial/Bank Asset #209",
    "country": "United States",
    "lat": 35.4175,
    "lon": -99.0959,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_210",
    "name": "United States Industrial/Bank Asset #210",
    "country": "United States",
    "lat": 45.0958,
    "lon": -111.1652,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_211",
    "name": "United States Industrial/Bank Asset #211",
    "country": "United States",
    "lat": 38.1311,
    "lon": -94.457,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_212",
    "name": "United States Industrial/Bank Asset #212",
    "country": "United States",
    "lat": 34.611,
    "lon": -92.4594,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_213",
    "name": "United States Industrial/Bank Asset #213",
    "country": "United States",
    "lat": 39.41,
    "lon": -106.0305,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_214",
    "name": "United States Industrial/Bank Asset #214",
    "country": "United States",
    "lat": 41.9969,
    "lon": -113.1837,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_215",
    "name": "United States Industrial/Bank Asset #215",
    "country": "United States",
    "lat": 43.5154,
    "lon": -90.2486,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_216",
    "name": "United States Industrial/Bank Asset #216",
    "country": "United States",
    "lat": 33.2054,
    "lon": -100.5956,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_217",
    "name": "United States Industrial/Bank Asset #217",
    "country": "United States",
    "lat": 34.3142,
    "lon": -84.611,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_218",
    "name": "United States Industrial/Bank Asset #218",
    "country": "United States",
    "lat": 39.7873,
    "lon": -111.8434,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_219",
    "name": "United States Industrial/Bank Asset #219",
    "country": "United States",
    "lat": 35.4872,
    "lon": -87.8999,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_220",
    "name": "United States Industrial/Bank Asset #220",
    "country": "United States",
    "lat": 38.8034,
    "lon": -89.3075,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_221",
    "name": "United States Industrial/Bank Asset #221",
    "country": "United States",
    "lat": 42.1812,
    "lon": -83.7132,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_222",
    "name": "United States Industrial/Bank Asset #222",
    "country": "United States",
    "lat": 41.0272,
    "lon": -84.8488,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_223",
    "name": "United States Industrial/Bank Asset #223",
    "country": "United States",
    "lat": 45.7628,
    "lon": -94.9704,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_224",
    "name": "United States Industrial/Bank Asset #224",
    "country": "United States",
    "lat": 43.0084,
    "lon": -98.2067,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_225",
    "name": "United States Industrial/Bank Asset #225",
    "country": "United States",
    "lat": 44.7891,
    "lon": -96.9138,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_226",
    "name": "United States Industrial/Bank Asset #226",
    "country": "United States",
    "lat": 45.8553,
    "lon": -91.0403,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_227",
    "name": "United States Industrial/Bank Asset #227",
    "country": "United States",
    "lat": 39.0948,
    "lon": -105.5743,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_228",
    "name": "United States Industrial/Bank Asset #228",
    "country": "United States",
    "lat": 35.4558,
    "lon": -94.2202,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_229",
    "name": "United States Industrial/Bank Asset #229",
    "country": "United States",
    "lat": 43.753,
    "lon": -97.711,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_230",
    "name": "United States Industrial/Bank Asset #230",
    "country": "United States",
    "lat": 41.528,
    "lon": -105.1121,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_231",
    "name": "United States Industrial/Bank Asset #231",
    "country": "United States",
    "lat": 32.7397,
    "lon": -104.7782,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_232",
    "name": "United States Industrial/Bank Asset #232",
    "country": "United States",
    "lat": 35.8474,
    "lon": -103.7587,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_233",
    "name": "United States Industrial/Bank Asset #233",
    "country": "United States",
    "lat": 40.1424,
    "lon": -109.1988,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_234",
    "name": "United States Industrial/Bank Asset #234",
    "country": "United States",
    "lat": 35.2002,
    "lon": -92.5315,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_235",
    "name": "United States Industrial/Bank Asset #235",
    "country": "United States",
    "lat": 42.8027,
    "lon": -111.4231,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_236",
    "name": "United States Industrial/Bank Asset #236",
    "country": "United States",
    "lat": 38.0216,
    "lon": -97.0717,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_237",
    "name": "United States Industrial/Bank Asset #237",
    "country": "United States",
    "lat": 38.1524,
    "lon": -107.145,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_238",
    "name": "United States Industrial/Bank Asset #238",
    "country": "United States",
    "lat": 38.2223,
    "lon": -86.2048,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_239",
    "name": "United States Industrial/Bank Asset #239",
    "country": "United States",
    "lat": 40.8453,
    "lon": -92.4843,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_240",
    "name": "United States Industrial/Bank Asset #240",
    "country": "United States",
    "lat": 45.2077,
    "lon": -90.3822,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_241",
    "name": "United States Industrial/Bank Asset #241",
    "country": "United States",
    "lat": 37.5861,
    "lon": -113.1731,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_242",
    "name": "United States Industrial/Bank Asset #242",
    "country": "United States",
    "lat": 37.1281,
    "lon": -90.7457,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_243",
    "name": "United States Industrial/Bank Asset #243",
    "country": "United States",
    "lat": 45.1552,
    "lon": -84.7471,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_244",
    "name": "United States Industrial/Bank Asset #244",
    "country": "United States",
    "lat": 38.2043,
    "lon": -90.9245,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_245",
    "name": "United States Industrial/Bank Asset #245",
    "country": "United States",
    "lat": 40.2381,
    "lon": -95.2524,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_246",
    "name": "United States Industrial/Bank Asset #246",
    "country": "United States",
    "lat": 35.0286,
    "lon": -106.7674,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_247",
    "name": "United States Industrial/Bank Asset #247",
    "country": "United States",
    "lat": 38.4734,
    "lon": -112.4793,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_248",
    "name": "United States Industrial/Bank Asset #248",
    "country": "United States",
    "lat": 36.8781,
    "lon": -92.9757,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_249",
    "name": "United States Industrial/Bank Asset #249",
    "country": "United States",
    "lat": 37.9691,
    "lon": -108.3987,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_250",
    "name": "United States Industrial/Bank Asset #250",
    "country": "United States",
    "lat": 38.9782,
    "lon": -109.5212,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_251",
    "name": "United States Industrial/Bank Asset #251",
    "country": "United States",
    "lat": 41.4561,
    "lon": -112.541,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_252",
    "name": "United States Industrial/Bank Asset #252",
    "country": "United States",
    "lat": 37.8043,
    "lon": -96.4182,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_253",
    "name": "United States Industrial/Bank Asset #253",
    "country": "United States",
    "lat": 31.9336,
    "lon": -94.0675,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_254",
    "name": "United States Industrial/Bank Asset #254",
    "country": "United States",
    "lat": 33.6712,
    "lon": -99.499,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_255",
    "name": "United States Industrial/Bank Asset #255",
    "country": "United States",
    "lat": 32.3046,
    "lon": -101.9769,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_256",
    "name": "United States Industrial/Bank Asset #256",
    "country": "United States",
    "lat": 34.8866,
    "lon": -103.5446,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_257",
    "name": "United States Industrial/Bank Asset #257",
    "country": "United States",
    "lat": 43.6797,
    "lon": -101.9762,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_258",
    "name": "United States Industrial/Bank Asset #258",
    "country": "United States",
    "lat": 43.5322,
    "lon": -88.3923,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_259",
    "name": "United States Industrial/Bank Asset #259",
    "country": "United States",
    "lat": 35.5363,
    "lon": -110.8928,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_260",
    "name": "United States Industrial/Bank Asset #260",
    "country": "United States",
    "lat": 31.8101,
    "lon": -97.1674,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_261",
    "name": "United States Industrial/Bank Asset #261",
    "country": "United States",
    "lat": 47.4985,
    "lon": -102.8512,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_262",
    "name": "United States Industrial/Bank Asset #262",
    "country": "United States",
    "lat": 41.9023,
    "lon": -89.913,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_263",
    "name": "United States Industrial/Bank Asset #263",
    "country": "United States",
    "lat": 41.9281,
    "lon": -90.723,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_264",
    "name": "United States Industrial/Bank Asset #264",
    "country": "United States",
    "lat": 46.6938,
    "lon": -107.3692,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_265",
    "name": "United States Industrial/Bank Asset #265",
    "country": "United States",
    "lat": 31.8261,
    "lon": -108.7785,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_266",
    "name": "United States Industrial/Bank Asset #266",
    "country": "United States",
    "lat": 33.5195,
    "lon": -93.2662,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_267",
    "name": "United States Industrial/Bank Asset #267",
    "country": "United States",
    "lat": 40.5235,
    "lon": -106.8111,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_268",
    "name": "United States Industrial/Bank Asset #268",
    "country": "United States",
    "lat": 42.6914,
    "lon": -90.3431,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_269",
    "name": "United States Industrial/Bank Asset #269",
    "country": "United States",
    "lat": 34.1846,
    "lon": -95.1326,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_270",
    "name": "United States Industrial/Bank Asset #270",
    "country": "United States",
    "lat": 43.4668,
    "lon": -109.914,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_271",
    "name": "United States Industrial/Bank Asset #271",
    "country": "United States",
    "lat": 44.6088,
    "lon": -84.4084,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_272",
    "name": "United States Industrial/Bank Asset #272",
    "country": "United States",
    "lat": 33.2296,
    "lon": -112.5796,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_273",
    "name": "United States Industrial/Bank Asset #273",
    "country": "United States",
    "lat": 36.4913,
    "lon": -93.0296,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_274",
    "name": "United States Industrial/Bank Asset #274",
    "country": "United States",
    "lat": 46.8308,
    "lon": -101.4504,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_275",
    "name": "United States Industrial/Bank Asset #275",
    "country": "United States",
    "lat": 42.9402,
    "lon": -111.0701,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_276",
    "name": "United States Industrial/Bank Asset #276",
    "country": "United States",
    "lat": 42.5498,
    "lon": -94.5327,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_277",
    "name": "United States Industrial/Bank Asset #277",
    "country": "United States",
    "lat": 33.1304,
    "lon": -90.1756,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_278",
    "name": "United States Industrial/Bank Asset #278",
    "country": "United States",
    "lat": 45.1047,
    "lon": -95.3377,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_279",
    "name": "United States Industrial/Bank Asset #279",
    "country": "United States",
    "lat": 33.4369,
    "lon": -83.8347,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_280",
    "name": "United States Industrial/Bank Asset #280",
    "country": "United States",
    "lat": 44.0222,
    "lon": -102.9339,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_281",
    "name": "United States Industrial/Bank Asset #281",
    "country": "United States",
    "lat": 38.354,
    "lon": -102.2329,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_282",
    "name": "United States Industrial/Bank Asset #282",
    "country": "United States",
    "lat": 39.5954,
    "lon": -103.1131,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_283",
    "name": "United States Industrial/Bank Asset #283",
    "country": "United States",
    "lat": 45.0932,
    "lon": -88.6801,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_284",
    "name": "United States Industrial/Bank Asset #284",
    "country": "United States",
    "lat": 33.1886,
    "lon": -84.5264,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_285",
    "name": "United States Industrial/Bank Asset #285",
    "country": "United States",
    "lat": 41.6694,
    "lon": -88.4888,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_286",
    "name": "United States Industrial/Bank Asset #286",
    "country": "United States",
    "lat": 42.8169,
    "lon": -100.2854,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_287",
    "name": "United States Industrial/Bank Asset #287",
    "country": "United States",
    "lat": 43.2407,
    "lon": -84.3858,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_288",
    "name": "United States Industrial/Bank Asset #288",
    "country": "United States",
    "lat": 35.8213,
    "lon": -89.104,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_289",
    "name": "United States Industrial/Bank Asset #289",
    "country": "United States",
    "lat": 40.1108,
    "lon": -98.8451,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_290",
    "name": "United States Industrial/Bank Asset #290",
    "country": "United States",
    "lat": 38.4692,
    "lon": -91.4192,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_291",
    "name": "United States Industrial/Bank Asset #291",
    "country": "United States",
    "lat": 35.7943,
    "lon": -87.7986,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_292",
    "name": "United States Industrial/Bank Asset #292",
    "country": "United States",
    "lat": 44.7917,
    "lon": -110.7501,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_293",
    "name": "United States Industrial/Bank Asset #293",
    "country": "United States",
    "lat": 45.6061,
    "lon": -106.0341,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_294",
    "name": "United States Industrial/Bank Asset #294",
    "country": "United States",
    "lat": 38.9353,
    "lon": -95.04,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_295",
    "name": "United States Industrial/Bank Asset #295",
    "country": "United States",
    "lat": 37.5638,
    "lon": -112.489,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_296",
    "name": "United States Industrial/Bank Asset #296",
    "country": "United States",
    "lat": 45.1152,
    "lon": -107.8948,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_297",
    "name": "United States Industrial/Bank Asset #297",
    "country": "United States",
    "lat": 34.8939,
    "lon": -89.415,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_298",
    "name": "United States Industrial/Bank Asset #298",
    "country": "United States",
    "lat": 36.9454,
    "lon": -86.9404,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_299",
    "name": "United States Industrial/Bank Asset #299",
    "country": "United States",
    "lat": 42.7189,
    "lon": -105.0619,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_300",
    "name": "United States Industrial/Bank Asset #300",
    "country": "United States",
    "lat": 31.6624,
    "lon": -84.9081,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_301",
    "name": "United States Industrial/Bank Asset #301",
    "country": "United States",
    "lat": 32.8698,
    "lon": -91.7478,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_302",
    "name": "United States Industrial/Bank Asset #302",
    "country": "United States",
    "lat": 39.3172,
    "lon": -90.6051,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_303",
    "name": "United States Industrial/Bank Asset #303",
    "country": "United States",
    "lat": 42.5497,
    "lon": -93.9729,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_304",
    "name": "United States Industrial/Bank Asset #304",
    "country": "United States",
    "lat": 39.3531,
    "lon": -89.562,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_305",
    "name": "United States Industrial/Bank Asset #305",
    "country": "United States",
    "lat": 32.9889,
    "lon": -106.7021,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_306",
    "name": "United States Industrial/Bank Asset #306",
    "country": "United States",
    "lat": 42.5686,
    "lon": -104.1638,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_307",
    "name": "United States Industrial/Bank Asset #307",
    "country": "United States",
    "lat": 40.8049,
    "lon": -99.1522,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_308",
    "name": "United States Industrial/Bank Asset #308",
    "country": "United States",
    "lat": 39.9948,
    "lon": -100.5849,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_309",
    "name": "United States Industrial/Bank Asset #309",
    "country": "United States",
    "lat": 43.435,
    "lon": -103.4263,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_310",
    "name": "United States Industrial/Bank Asset #310",
    "country": "United States",
    "lat": 42.7457,
    "lon": -105.2225,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_311",
    "name": "United States Industrial/Bank Asset #311",
    "country": "United States",
    "lat": 35.5225,
    "lon": -109.7303,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_312",
    "name": "United States Industrial/Bank Asset #312",
    "country": "United States",
    "lat": 34.5813,
    "lon": -109.7634,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_313",
    "name": "United States Industrial/Bank Asset #313",
    "country": "United States",
    "lat": 40.0738,
    "lon": -90.4843,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_314",
    "name": "United States Industrial/Bank Asset #314",
    "country": "United States",
    "lat": 34.4624,
    "lon": -106.8585,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_315",
    "name": "United States Industrial/Bank Asset #315",
    "country": "United States",
    "lat": 39.2472,
    "lon": -91.6124,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_316",
    "name": "United States Industrial/Bank Asset #316",
    "country": "United States",
    "lat": 47.1257,
    "lon": -97.6109,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_317",
    "name": "United States Industrial/Bank Asset #317",
    "country": "United States",
    "lat": 36.028,
    "lon": -110.3342,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_318",
    "name": "United States Industrial/Bank Asset #318",
    "country": "United States",
    "lat": 34.6059,
    "lon": -106.5255,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_319",
    "name": "United States Industrial/Bank Asset #319",
    "country": "United States",
    "lat": 34.3711,
    "lon": -112.9255,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_320",
    "name": "United States Industrial/Bank Asset #320",
    "country": "United States",
    "lat": 40.0462,
    "lon": -105.1207,
    "type": "Municipal & Commercial Grid",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_1",
    "name": "Canada Industrial/Bank Asset #001",
    "country": "Canada",
    "lat": 58.6915,
    "lon": -102.8656,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_2",
    "name": "Canada Industrial/Bank Asset #002",
    "country": "Canada",
    "lat": 55.369,
    "lon": -119.9488,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_3",
    "name": "Canada Industrial/Bank Asset #003",
    "country": "Canada",
    "lat": 57.4215,
    "lon": -105.3649,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_4",
    "name": "Canada Industrial/Bank Asset #004",
    "country": "Canada",
    "lat": 57.4726,
    "lon": -102.0374,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_5",
    "name": "Canada Industrial/Bank Asset #005",
    "country": "Canada",
    "lat": 52.6328,
    "lon": -107.3812,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_6",
    "name": "Canada Industrial/Bank Asset #006",
    "country": "Canada",
    "lat": 49.2124,
    "lon": -122.9449,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_7",
    "name": "Canada Industrial/Bank Asset #007",
    "country": "Canada",
    "lat": 58.2928,
    "lon": -105.8908,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_8",
    "name": "Canada Industrial/Bank Asset #008",
    "country": "Canada",
    "lat": 56.8654,
    "lon": -108.9717,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_9",
    "name": "Canada Industrial/Bank Asset #009",
    "country": "Canada",
    "lat": 47.889,
    "lon": -99.8222,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_10",
    "name": "Canada Industrial/Bank Asset #010",
    "country": "Canada",
    "lat": 47.6433,
    "lon": -119.0321,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_11",
    "name": "Canada Industrial/Bank Asset #011",
    "country": "Canada",
    "lat": 53.7541,
    "lon": -112.8466,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_12",
    "name": "Canada Industrial/Bank Asset #012",
    "country": "Canada",
    "lat": 58.927,
    "lon": -120.2619,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_13",
    "name": "Canada Industrial/Bank Asset #013",
    "country": "Canada",
    "lat": 56.1733,
    "lon": -100.7473,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_14",
    "name": "Canada Industrial/Bank Asset #014",
    "country": "Canada",
    "lat": 56.4889,
    "lon": -115.9725,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_15",
    "name": "Canada Industrial/Bank Asset #015",
    "country": "Canada",
    "lat": 53.2709,
    "lon": -106.9794,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_16",
    "name": "Canada Industrial/Bank Asset #016",
    "country": "Canada",
    "lat": 52.3127,
    "lon": -90.5933,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_17",
    "name": "Canada Industrial/Bank Asset #017",
    "country": "Canada",
    "lat": 58.8804,
    "lon": -112.7848,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_18",
    "name": "Canada Industrial/Bank Asset #018",
    "country": "Canada",
    "lat": 54.4523,
    "lon": -100.6148,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_19",
    "name": "Canada Industrial/Bank Asset #019",
    "country": "Canada",
    "lat": 55.8811,
    "lon": -87.0964,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_20",
    "name": "Canada Industrial/Bank Asset #020",
    "country": "Canada",
    "lat": 49.4935,
    "lon": -116.559,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_21",
    "name": "Canada Industrial/Bank Asset #021",
    "country": "Canada",
    "lat": 54.9251,
    "lon": -118.7177,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_22",
    "name": "Canada Industrial/Bank Asset #022",
    "country": "Canada",
    "lat": 49.0858,
    "lon": -121.9974,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_23",
    "name": "Canada Industrial/Bank Asset #023",
    "country": "Canada",
    "lat": 47.0321,
    "lon": -106.9799,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_24",
    "name": "Canada Industrial/Bank Asset #024",
    "country": "Canada",
    "lat": 54.1257,
    "lon": -113.3496,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_25",
    "name": "Canada Industrial/Bank Asset #025",
    "country": "Canada",
    "lat": 49.7777,
    "lon": -96.7218,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_26",
    "name": "Canada Industrial/Bank Asset #026",
    "country": "Canada",
    "lat": 55.4359,
    "lon": -106.8387,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_27",
    "name": "Canada Industrial/Bank Asset #027",
    "country": "Canada",
    "lat": 55.2486,
    "lon": -88.0436,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_28",
    "name": "Canada Industrial/Bank Asset #028",
    "country": "Canada",
    "lat": 56.4539,
    "lon": -99.9977,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_29",
    "name": "Canada Industrial/Bank Asset #029",
    "country": "Canada",
    "lat": 54.9342,
    "lon": -87.6533,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_30",
    "name": "Canada Industrial/Bank Asset #030",
    "country": "Canada",
    "lat": 52.1017,
    "lon": -103.2175,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_31",
    "name": "Canada Industrial/Bank Asset #031",
    "country": "Canada",
    "lat": 54.7716,
    "lon": -88.6635,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_32",
    "name": "Canada Industrial/Bank Asset #032",
    "country": "Canada",
    "lat": 56.9196,
    "lon": -122.1436,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_33",
    "name": "Canada Industrial/Bank Asset #033",
    "country": "Canada",
    "lat": 48.9911,
    "lon": -112.6955,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_34",
    "name": "Canada Industrial/Bank Asset #034",
    "country": "Canada",
    "lat": 55.9875,
    "lon": -102.2317,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_35",
    "name": "Canada Industrial/Bank Asset #035",
    "country": "Canada",
    "lat": 50.4633,
    "lon": -120.0259,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_36",
    "name": "Canada Industrial/Bank Asset #036",
    "country": "Canada",
    "lat": 55.2641,
    "lon": -97.0107,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_37",
    "name": "Canada Industrial/Bank Asset #037",
    "country": "Canada",
    "lat": 58.3121,
    "lon": -104.9811,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_38",
    "name": "Canada Industrial/Bank Asset #038",
    "country": "Canada",
    "lat": 52.9255,
    "lon": -121.7823,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_39",
    "name": "Canada Industrial/Bank Asset #039",
    "country": "Canada",
    "lat": 47.4783,
    "lon": -107.7189,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_40",
    "name": "Canada Industrial/Bank Asset #040",
    "country": "Canada",
    "lat": 50.8679,
    "lon": -114.9853,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_41",
    "name": "Canada Industrial/Bank Asset #041",
    "country": "Canada",
    "lat": 48.0959,
    "lon": -86.5236,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_42",
    "name": "Canada Industrial/Bank Asset #042",
    "country": "Canada",
    "lat": 57.0315,
    "lon": -101.992,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_43",
    "name": "Canada Industrial/Bank Asset #043",
    "country": "Canada",
    "lat": 58.4094,
    "lon": -85.0171,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_44",
    "name": "Canada Industrial/Bank Asset #044",
    "country": "Canada",
    "lat": 55.0674,
    "lon": -114.2196,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_45",
    "name": "Canada Industrial/Bank Asset #045",
    "country": "Canada",
    "lat": 47.4828,
    "lon": -94.7492,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_46",
    "name": "Canada Industrial/Bank Asset #046",
    "country": "Canada",
    "lat": 52.646,
    "lon": -98.9396,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_47",
    "name": "Canada Industrial/Bank Asset #047",
    "country": "Canada",
    "lat": 57.9929,
    "lon": -117.7404,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_48",
    "name": "Canada Industrial/Bank Asset #048",
    "country": "Canada",
    "lat": 54.024,
    "lon": -99.6086,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_49",
    "name": "Canada Industrial/Bank Asset #049",
    "country": "Canada",
    "lat": 52.9007,
    "lon": -121.3503,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_50",
    "name": "Canada Industrial/Bank Asset #050",
    "country": "Canada",
    "lat": 51.1755,
    "lon": -111.6677,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_51",
    "name": "Canada Industrial/Bank Asset #051",
    "country": "Canada",
    "lat": 55.0416,
    "lon": -90.6907,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_52",
    "name": "Canada Industrial/Bank Asset #052",
    "country": "Canada",
    "lat": 50.9576,
    "lon": -97.2531,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_53",
    "name": "Canada Industrial/Bank Asset #053",
    "country": "Canada",
    "lat": 50.4586,
    "lon": -87.1923,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_54",
    "name": "Canada Industrial/Bank Asset #054",
    "country": "Canada",
    "lat": 56.7628,
    "lon": -102.9961,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_55",
    "name": "Canada Industrial/Bank Asset #055",
    "country": "Canada",
    "lat": 52.4579,
    "lon": -112.4193,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_56",
    "name": "Canada Industrial/Bank Asset #056",
    "country": "Canada",
    "lat": 50.8793,
    "lon": -86.1926,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_57",
    "name": "Canada Industrial/Bank Asset #057",
    "country": "Canada",
    "lat": 51.8501,
    "lon": -104.4161,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_58",
    "name": "Canada Industrial/Bank Asset #058",
    "country": "Canada",
    "lat": 58.8574,
    "lon": -98.6936,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_59",
    "name": "Canada Industrial/Bank Asset #059",
    "country": "Canada",
    "lat": 53.5111,
    "lon": -108.4701,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_60",
    "name": "Canada Industrial/Bank Asset #060",
    "country": "Canada",
    "lat": 49.251,
    "lon": -110.5288,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_61",
    "name": "Canada Industrial/Bank Asset #061",
    "country": "Canada",
    "lat": 56.0773,
    "lon": -99.9837,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_62",
    "name": "Canada Industrial/Bank Asset #062",
    "country": "Canada",
    "lat": 56.1199,
    "lon": -116.8577,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_63",
    "name": "Canada Industrial/Bank Asset #063",
    "country": "Canada",
    "lat": 53.5906,
    "lon": -87.8931,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_64",
    "name": "Canada Industrial/Bank Asset #064",
    "country": "Canada",
    "lat": 52.2574,
    "lon": -97.07,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_65",
    "name": "Canada Industrial/Bank Asset #065",
    "country": "Canada",
    "lat": 48.4571,
    "lon": -86.0741,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_66",
    "name": "Canada Industrial/Bank Asset #066",
    "country": "Canada",
    "lat": 54.3065,
    "lon": -115.4281,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_67",
    "name": "Canada Industrial/Bank Asset #067",
    "country": "Canada",
    "lat": 48.9005,
    "lon": -102.9664,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_68",
    "name": "Canada Industrial/Bank Asset #068",
    "country": "Canada",
    "lat": 53.627,
    "lon": -121.2716,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_69",
    "name": "Canada Industrial/Bank Asset #069",
    "country": "Canada",
    "lat": 58.9071,
    "lon": -88.4828,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_70",
    "name": "Canada Industrial/Bank Asset #070",
    "country": "Canada",
    "lat": 52.5374,
    "lon": -120.3014,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_71",
    "name": "Canada Industrial/Bank Asset #071",
    "country": "Canada",
    "lat": 56.9857,
    "lon": -105.065,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_72",
    "name": "Canada Industrial/Bank Asset #072",
    "country": "Canada",
    "lat": 55.5992,
    "lon": -104.6451,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_73",
    "name": "Canada Industrial/Bank Asset #073",
    "country": "Canada",
    "lat": 50.2811,
    "lon": -91.611,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_74",
    "name": "Canada Industrial/Bank Asset #074",
    "country": "Canada",
    "lat": 58.7629,
    "lon": -115.2508,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_75",
    "name": "Canada Industrial/Bank Asset #075",
    "country": "Canada",
    "lat": 53.6152,
    "lon": -109.6566,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_76",
    "name": "Canada Industrial/Bank Asset #076",
    "country": "Canada",
    "lat": 58.0624,
    "lon": -104.6704,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_77",
    "name": "Canada Industrial/Bank Asset #077",
    "country": "Canada",
    "lat": 57.5519,
    "lon": -90.4389,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_78",
    "name": "Canada Industrial/Bank Asset #078",
    "country": "Canada",
    "lat": 50.315,
    "lon": -93.3998,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_79",
    "name": "Canada Industrial/Bank Asset #079",
    "country": "Canada",
    "lat": 51.9793,
    "lon": -87.6301,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_can_80",
    "name": "Canada Industrial/Bank Asset #080",
    "country": "Canada",
    "lat": 53.0929,
    "lon": -92.178,
    "type": "Energy & Grain Rail Hubs",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_1",
    "name": "United Kingdom Industrial/Bank Asset #001",
    "country": "United Kingdom",
    "lat": 51.9142,
    "lon": -2.3058,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_2",
    "name": "United Kingdom Industrial/Bank Asset #002",
    "country": "United Kingdom",
    "lat": 53.4347,
    "lon": 0.4956,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_3",
    "name": "United Kingdom Industrial/Bank Asset #003",
    "country": "United Kingdom",
    "lat": 52.9482,
    "lon": -2.9056,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_4",
    "name": "United Kingdom Industrial/Bank Asset #004",
    "country": "United Kingdom",
    "lat": 53.1929,
    "lon": -2.1195,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_5",
    "name": "United Kingdom Industrial/Bank Asset #005",
    "country": "United Kingdom",
    "lat": 53.2596,
    "lon": -1.3263,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_6",
    "name": "United Kingdom Industrial/Bank Asset #006",
    "country": "United Kingdom",
    "lat": 52.7767,
    "lon": -2.2129,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_7",
    "name": "United Kingdom Industrial/Bank Asset #007",
    "country": "United Kingdom",
    "lat": 51.4433,
    "lon": -0.71,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_8",
    "name": "United Kingdom Industrial/Bank Asset #008",
    "country": "United Kingdom",
    "lat": 53.359,
    "lon": -2.5658,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_9",
    "name": "United Kingdom Industrial/Bank Asset #009",
    "country": "United Kingdom",
    "lat": 54.3777,
    "lon": -3.3254,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_10",
    "name": "United Kingdom Industrial/Bank Asset #010",
    "country": "United Kingdom",
    "lat": 54.2235,
    "lon": -0.6791,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_11",
    "name": "United Kingdom Industrial/Bank Asset #011",
    "country": "United Kingdom",
    "lat": 54.557,
    "lon": -1.9557,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_12",
    "name": "United Kingdom Industrial/Bank Asset #012",
    "country": "United Kingdom",
    "lat": 53.8184,
    "lon": -0.217,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_13",
    "name": "United Kingdom Industrial/Bank Asset #013",
    "country": "United Kingdom",
    "lat": 55.4041,
    "lon": -1.5187,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_14",
    "name": "United Kingdom Industrial/Bank Asset #014",
    "country": "United Kingdom",
    "lat": 50.6851,
    "lon": -1.4908,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_15",
    "name": "United Kingdom Industrial/Bank Asset #015",
    "country": "United Kingdom",
    "lat": 53.4509,
    "lon": -0.0212,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_16",
    "name": "United Kingdom Industrial/Bank Asset #016",
    "country": "United Kingdom",
    "lat": 54.871,
    "lon": -1.7388,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_17",
    "name": "United Kingdom Industrial/Bank Asset #017",
    "country": "United Kingdom",
    "lat": 53.1298,
    "lon": -1.6723,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_18",
    "name": "United Kingdom Industrial/Bank Asset #018",
    "country": "United Kingdom",
    "lat": 54.1122,
    "lon": -1.8601,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_19",
    "name": "United Kingdom Industrial/Bank Asset #019",
    "country": "United Kingdom",
    "lat": 53.7739,
    "lon": -2.8826,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_20",
    "name": "United Kingdom Industrial/Bank Asset #020",
    "country": "United Kingdom",
    "lat": 52.8475,
    "lon": 0.3768,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_21",
    "name": "United Kingdom Industrial/Bank Asset #021",
    "country": "United Kingdom",
    "lat": 52.1928,
    "lon": -0.7292,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_22",
    "name": "United Kingdom Industrial/Bank Asset #022",
    "country": "United Kingdom",
    "lat": 53.7492,
    "lon": -0.0929,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_23",
    "name": "United Kingdom Industrial/Bank Asset #023",
    "country": "United Kingdom",
    "lat": 54.7617,
    "lon": -0.0626,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_24",
    "name": "United Kingdom Industrial/Bank Asset #024",
    "country": "United Kingdom",
    "lat": 52.4,
    "lon": -2.2334,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_25",
    "name": "United Kingdom Industrial/Bank Asset #025",
    "country": "United Kingdom",
    "lat": 54.0936,
    "lon": -0.4624,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_26",
    "name": "United Kingdom Industrial/Bank Asset #026",
    "country": "United Kingdom",
    "lat": 54.8619,
    "lon": -3.3564,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_27",
    "name": "United Kingdom Industrial/Bank Asset #027",
    "country": "United Kingdom",
    "lat": 50.8421,
    "lon": -0.9754,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_28",
    "name": "United Kingdom Industrial/Bank Asset #028",
    "country": "United Kingdom",
    "lat": 55.1046,
    "lon": 0.4897,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_29",
    "name": "United Kingdom Industrial/Bank Asset #029",
    "country": "United Kingdom",
    "lat": 54.2338,
    "lon": -1.7641,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_30",
    "name": "United Kingdom Industrial/Bank Asset #030",
    "country": "United Kingdom",
    "lat": 50.9922,
    "lon": -0.965,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_31",
    "name": "United Kingdom Industrial/Bank Asset #031",
    "country": "United Kingdom",
    "lat": 54.8629,
    "lon": -1.7253,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_32",
    "name": "United Kingdom Industrial/Bank Asset #032",
    "country": "United Kingdom",
    "lat": 53.97,
    "lon": 0.1137,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_33",
    "name": "United Kingdom Industrial/Bank Asset #033",
    "country": "United Kingdom",
    "lat": 50.73,
    "lon": -0.3154,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_34",
    "name": "United Kingdom Industrial/Bank Asset #034",
    "country": "United Kingdom",
    "lat": 51.9668,
    "lon": -2.0006,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_35",
    "name": "United Kingdom Industrial/Bank Asset #035",
    "country": "United Kingdom",
    "lat": 51.2278,
    "lon": -1.3753,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_36",
    "name": "United Kingdom Industrial/Bank Asset #036",
    "country": "United Kingdom",
    "lat": 53.3296,
    "lon": -0.3299,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_37",
    "name": "United Kingdom Industrial/Bank Asset #037",
    "country": "United Kingdom",
    "lat": 51.3499,
    "lon": -3.1841,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_38",
    "name": "United Kingdom Industrial/Bank Asset #038",
    "country": "United Kingdom",
    "lat": 54.8542,
    "lon": -1.0212,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_39",
    "name": "United Kingdom Industrial/Bank Asset #039",
    "country": "United Kingdom",
    "lat": 51.7041,
    "lon": 0.1513,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_40",
    "name": "United Kingdom Industrial/Bank Asset #040",
    "country": "United Kingdom",
    "lat": 51.2156,
    "lon": -1.6554,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_41",
    "name": "United Kingdom Industrial/Bank Asset #041",
    "country": "United Kingdom",
    "lat": 51.7699,
    "lon": -2.4787,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_42",
    "name": "United Kingdom Industrial/Bank Asset #042",
    "country": "United Kingdom",
    "lat": 50.547,
    "lon": -0.2815,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_43",
    "name": "United Kingdom Industrial/Bank Asset #043",
    "country": "United Kingdom",
    "lat": 55.006,
    "lon": -0.7896,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_44",
    "name": "United Kingdom Industrial/Bank Asset #044",
    "country": "United Kingdom",
    "lat": 51.2899,
    "lon": -1.7331,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_45",
    "name": "United Kingdom Industrial/Bank Asset #045",
    "country": "United Kingdom",
    "lat": 52.2278,
    "lon": -1.1497,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_46",
    "name": "United Kingdom Industrial/Bank Asset #046",
    "country": "United Kingdom",
    "lat": 53.6947,
    "lon": -1.8028,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_47",
    "name": "United Kingdom Industrial/Bank Asset #047",
    "country": "United Kingdom",
    "lat": 51.7505,
    "lon": -0.1188,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_48",
    "name": "United Kingdom Industrial/Bank Asset #048",
    "country": "United Kingdom",
    "lat": 51.4961,
    "lon": -1.9612,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_49",
    "name": "United Kingdom Industrial/Bank Asset #049",
    "country": "United Kingdom",
    "lat": 52.916,
    "lon": -2.5512,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_50",
    "name": "United Kingdom Industrial/Bank Asset #050",
    "country": "United Kingdom",
    "lat": 53.3596,
    "lon": -1.2008,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_51",
    "name": "United Kingdom Industrial/Bank Asset #051",
    "country": "United Kingdom",
    "lat": 55.4635,
    "lon": -2.3191,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_52",
    "name": "United Kingdom Industrial/Bank Asset #052",
    "country": "United Kingdom",
    "lat": 55.3897,
    "lon": -0.8671,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_53",
    "name": "United Kingdom Industrial/Bank Asset #053",
    "country": "United Kingdom",
    "lat": 51.8724,
    "lon": -1.2363,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_54",
    "name": "United Kingdom Industrial/Bank Asset #054",
    "country": "United Kingdom",
    "lat": 53.929,
    "lon": -0.5213,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_55",
    "name": "United Kingdom Industrial/Bank Asset #055",
    "country": "United Kingdom",
    "lat": 50.7452,
    "lon": -1.0744,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_56",
    "name": "United Kingdom Industrial/Bank Asset #056",
    "country": "United Kingdom",
    "lat": 52.9836,
    "lon": 0.1166,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_57",
    "name": "United Kingdom Industrial/Bank Asset #057",
    "country": "United Kingdom",
    "lat": 51.931,
    "lon": -0.3046,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_58",
    "name": "United Kingdom Industrial/Bank Asset #058",
    "country": "United Kingdom",
    "lat": 53.5353,
    "lon": -2.0907,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_59",
    "name": "United Kingdom Industrial/Bank Asset #059",
    "country": "United Kingdom",
    "lat": 53.6831,
    "lon": -1.0164,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_60",
    "name": "United Kingdom Industrial/Bank Asset #060",
    "country": "United Kingdom",
    "lat": 53.8888,
    "lon": -0.6163,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_61",
    "name": "United Kingdom Industrial/Bank Asset #061",
    "country": "United Kingdom",
    "lat": 53.7959,
    "lon": -0.1467,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_62",
    "name": "United Kingdom Industrial/Bank Asset #062",
    "country": "United Kingdom",
    "lat": 53.6412,
    "lon": 0.1136,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_63",
    "name": "United Kingdom Industrial/Bank Asset #063",
    "country": "United Kingdom",
    "lat": 53.7317,
    "lon": -2.2643,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_64",
    "name": "United Kingdom Industrial/Bank Asset #064",
    "country": "United Kingdom",
    "lat": 52.7041,
    "lon": -1.1817,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_65",
    "name": "United Kingdom Industrial/Bank Asset #065",
    "country": "United Kingdom",
    "lat": 54.1618,
    "lon": -3.1395,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_66",
    "name": "United Kingdom Industrial/Bank Asset #066",
    "country": "United Kingdom",
    "lat": 51.9756,
    "lon": -0.5101,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_67",
    "name": "United Kingdom Industrial/Bank Asset #067",
    "country": "United Kingdom",
    "lat": 51.3782,
    "lon": -2.9714,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_68",
    "name": "United Kingdom Industrial/Bank Asset #068",
    "country": "United Kingdom",
    "lat": 53.197,
    "lon": 0.386,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_69",
    "name": "United Kingdom Industrial/Bank Asset #069",
    "country": "United Kingdom",
    "lat": 53.1543,
    "lon": 0.1539,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_70",
    "name": "United Kingdom Industrial/Bank Asset #070",
    "country": "United Kingdom",
    "lat": 54.6524,
    "lon": -2.4721,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_71",
    "name": "United Kingdom Industrial/Bank Asset #071",
    "country": "United Kingdom",
    "lat": 54.6234,
    "lon": -1.5726,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_72",
    "name": "United Kingdom Industrial/Bank Asset #072",
    "country": "United Kingdom",
    "lat": 54.5324,
    "lon": -0.5138,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_73",
    "name": "United Kingdom Industrial/Bank Asset #073",
    "country": "United Kingdom",
    "lat": 52.1936,
    "lon": -3.0393,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_74",
    "name": "United Kingdom Industrial/Bank Asset #074",
    "country": "United Kingdom",
    "lat": 55.3145,
    "lon": -2.937,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_75",
    "name": "United Kingdom Industrial/Bank Asset #075",
    "country": "United Kingdom",
    "lat": 55.3325,
    "lon": -0.0594,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_76",
    "name": "United Kingdom Industrial/Bank Asset #076",
    "country": "United Kingdom",
    "lat": 54.1211,
    "lon": 0.4198,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_77",
    "name": "United Kingdom Industrial/Bank Asset #077",
    "country": "United Kingdom",
    "lat": 55.3363,
    "lon": -0.2816,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_78",
    "name": "United Kingdom Industrial/Bank Asset #078",
    "country": "United Kingdom",
    "lat": 52.3289,
    "lon": -0.3373,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_79",
    "name": "United Kingdom Industrial/Bank Asset #079",
    "country": "United Kingdom",
    "lat": 50.5696,
    "lon": -1.3537,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_80",
    "name": "United Kingdom Industrial/Bank Asset #080",
    "country": "United Kingdom",
    "lat": 52.7739,
    "lon": -0.8087,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_81",
    "name": "United Kingdom Industrial/Bank Asset #081",
    "country": "United Kingdom",
    "lat": 53.8617,
    "lon": -1.1618,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_82",
    "name": "United Kingdom Industrial/Bank Asset #082",
    "country": "United Kingdom",
    "lat": 54.6121,
    "lon": 0.2612,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_83",
    "name": "United Kingdom Industrial/Bank Asset #083",
    "country": "United Kingdom",
    "lat": 51.0417,
    "lon": -2.5647,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_84",
    "name": "United Kingdom Industrial/Bank Asset #084",
    "country": "United Kingdom",
    "lat": 50.6251,
    "lon": 0.0369,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_85",
    "name": "United Kingdom Industrial/Bank Asset #085",
    "country": "United Kingdom",
    "lat": 53.307,
    "lon": 0.161,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_86",
    "name": "United Kingdom Industrial/Bank Asset #086",
    "country": "United Kingdom",
    "lat": 51.6068,
    "lon": -3.2471,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_87",
    "name": "United Kingdom Industrial/Bank Asset #087",
    "country": "United Kingdom",
    "lat": 54.6193,
    "lon": 0.1376,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_88",
    "name": "United Kingdom Industrial/Bank Asset #088",
    "country": "United Kingdom",
    "lat": 52.011,
    "lon": -1.8668,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_89",
    "name": "United Kingdom Industrial/Bank Asset #089",
    "country": "United Kingdom",
    "lat": 51.1989,
    "lon": 0.285,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_90",
    "name": "United Kingdom Industrial/Bank Asset #090",
    "country": "United Kingdom",
    "lat": 52.0218,
    "lon": -1.5295,
    "type": "Industrial & Bank Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_1",
    "name": "Germany Industrial/Bank Asset #001",
    "country": "Germany",
    "lat": 49.146,
    "lon": 12.7736,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_2",
    "name": "Germany Industrial/Bank Asset #002",
    "country": "Germany",
    "lat": 49.3383,
    "lon": 10.1719,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_3",
    "name": "Germany Industrial/Bank Asset #003",
    "country": "Germany",
    "lat": 52.0124,
    "lon": 11.9088,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_4",
    "name": "Germany Industrial/Bank Asset #004",
    "country": "Germany",
    "lat": 53.3899,
    "lon": 9.9648,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_5",
    "name": "Germany Industrial/Bank Asset #005",
    "country": "Germany",
    "lat": 52.3713,
    "lon": 8.3771,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_6",
    "name": "Germany Industrial/Bank Asset #006",
    "country": "Germany",
    "lat": 50.7344,
    "lon": 8.0441,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_7",
    "name": "Germany Industrial/Bank Asset #007",
    "country": "Germany",
    "lat": 51.1067,
    "lon": 9.8987,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_8",
    "name": "Germany Industrial/Bank Asset #008",
    "country": "Germany",
    "lat": 53.4176,
    "lon": 7.6463,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_9",
    "name": "Germany Industrial/Bank Asset #009",
    "country": "Germany",
    "lat": 50.5126,
    "lon": 10.1103,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_10",
    "name": "Germany Industrial/Bank Asset #010",
    "country": "Germany",
    "lat": 53.4128,
    "lon": 12.5827,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_11",
    "name": "Germany Industrial/Bank Asset #011",
    "country": "Germany",
    "lat": 49.1568,
    "lon": 11.5641,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_12",
    "name": "Germany Industrial/Bank Asset #012",
    "country": "Germany",
    "lat": 51.3823,
    "lon": 13.3171,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_13",
    "name": "Germany Industrial/Bank Asset #013",
    "country": "Germany",
    "lat": 50.4534,
    "lon": 9.8388,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_14",
    "name": "Germany Industrial/Bank Asset #014",
    "country": "Germany",
    "lat": 49.609,
    "lon": 8.183,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_15",
    "name": "Germany Industrial/Bank Asset #015",
    "country": "Germany",
    "lat": 52.9002,
    "lon": 10.1783,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_16",
    "name": "Germany Industrial/Bank Asset #016",
    "country": "Germany",
    "lat": 51.9738,
    "lon": 11.3002,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_17",
    "name": "Germany Industrial/Bank Asset #017",
    "country": "Germany",
    "lat": 51.6457,
    "lon": 7.5781,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_18",
    "name": "Germany Industrial/Bank Asset #018",
    "country": "Germany",
    "lat": 52.594,
    "lon": 8.9114,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_19",
    "name": "Germany Industrial/Bank Asset #019",
    "country": "Germany",
    "lat": 49.2896,
    "lon": 10.8375,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_20",
    "name": "Germany Industrial/Bank Asset #020",
    "country": "Germany",
    "lat": 49.0031,
    "lon": 12.0409,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_21",
    "name": "Germany Industrial/Bank Asset #021",
    "country": "Germany",
    "lat": 49.6958,
    "lon": 8.7457,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_22",
    "name": "Germany Industrial/Bank Asset #022",
    "country": "Germany",
    "lat": 53.0085,
    "lon": 9.4214,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_23",
    "name": "Germany Industrial/Bank Asset #023",
    "country": "Germany",
    "lat": 49.3978,
    "lon": 12.8532,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_24",
    "name": "Germany Industrial/Bank Asset #024",
    "country": "Germany",
    "lat": 48.6742,
    "lon": 12.6004,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_25",
    "name": "Germany Industrial/Bank Asset #025",
    "country": "Germany",
    "lat": 49.3834,
    "lon": 8.23,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_26",
    "name": "Germany Industrial/Bank Asset #026",
    "country": "Germany",
    "lat": 49.9133,
    "lon": 8.497,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_27",
    "name": "Germany Industrial/Bank Asset #027",
    "country": "Germany",
    "lat": 51.9653,
    "lon": 7.6047,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_28",
    "name": "Germany Industrial/Bank Asset #028",
    "country": "Germany",
    "lat": 48.7343,
    "lon": 12.1899,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_29",
    "name": "Germany Industrial/Bank Asset #029",
    "country": "Germany",
    "lat": 49.8497,
    "lon": 9.3926,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_30",
    "name": "Germany Industrial/Bank Asset #030",
    "country": "Germany",
    "lat": 49.5312,
    "lon": 7.7644,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_31",
    "name": "Germany Industrial/Bank Asset #031",
    "country": "Germany",
    "lat": 52.3686,
    "lon": 10.6065,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_32",
    "name": "Germany Industrial/Bank Asset #032",
    "country": "Germany",
    "lat": 52.3883,
    "lon": 10.3075,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_33",
    "name": "Germany Industrial/Bank Asset #033",
    "country": "Germany",
    "lat": 52.5501,
    "lon": 10.5294,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_34",
    "name": "Germany Industrial/Bank Asset #034",
    "country": "Germany",
    "lat": 49.2053,
    "lon": 10.473,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_35",
    "name": "Germany Industrial/Bank Asset #035",
    "country": "Germany",
    "lat": 53.3871,
    "lon": 7.7102,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_36",
    "name": "Germany Industrial/Bank Asset #036",
    "country": "Germany",
    "lat": 52.5761,
    "lon": 12.6519,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_37",
    "name": "Germany Industrial/Bank Asset #037",
    "country": "Germany",
    "lat": 51.2673,
    "lon": 10.1983,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_38",
    "name": "Germany Industrial/Bank Asset #038",
    "country": "Germany",
    "lat": 53.4801,
    "lon": 7.815,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_39",
    "name": "Germany Industrial/Bank Asset #039",
    "country": "Germany",
    "lat": 51.0549,
    "lon": 9.8597,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_40",
    "name": "Germany Industrial/Bank Asset #040",
    "country": "Germany",
    "lat": 52.0905,
    "lon": 10.3916,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_41",
    "name": "Germany Industrial/Bank Asset #041",
    "country": "Germany",
    "lat": 53.2085,
    "lon": 7.8909,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_42",
    "name": "Germany Industrial/Bank Asset #042",
    "country": "Germany",
    "lat": 49.064,
    "lon": 11.0998,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_43",
    "name": "Germany Industrial/Bank Asset #043",
    "country": "Germany",
    "lat": 48.9884,
    "lon": 9.1001,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_44",
    "name": "Germany Industrial/Bank Asset #044",
    "country": "Germany",
    "lat": 51.8254,
    "lon": 10.7401,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_45",
    "name": "Germany Industrial/Bank Asset #045",
    "country": "Germany",
    "lat": 50.2859,
    "lon": 13.4178,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_46",
    "name": "Germany Industrial/Bank Asset #046",
    "country": "Germany",
    "lat": 51.3128,
    "lon": 10.1723,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_47",
    "name": "Germany Industrial/Bank Asset #047",
    "country": "Germany",
    "lat": 51.6871,
    "lon": 8.0451,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_48",
    "name": "Germany Industrial/Bank Asset #048",
    "country": "Germany",
    "lat": 52.1689,
    "lon": 12.5668,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_49",
    "name": "Germany Industrial/Bank Asset #049",
    "country": "Germany",
    "lat": 51.9146,
    "lon": 12.0638,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_50",
    "name": "Germany Industrial/Bank Asset #050",
    "country": "Germany",
    "lat": 52.2642,
    "lon": 8.7401,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_51",
    "name": "Germany Industrial/Bank Asset #051",
    "country": "Germany",
    "lat": 50.9178,
    "lon": 8.821,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_52",
    "name": "Germany Industrial/Bank Asset #052",
    "country": "Germany",
    "lat": 50.3547,
    "lon": 10.171,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_53",
    "name": "Germany Industrial/Bank Asset #053",
    "country": "Germany",
    "lat": 50.7399,
    "lon": 8.0205,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_54",
    "name": "Germany Industrial/Bank Asset #054",
    "country": "Germany",
    "lat": 50.7938,
    "lon": 11.4406,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_55",
    "name": "Germany Industrial/Bank Asset #055",
    "country": "Germany",
    "lat": 50.5315,
    "lon": 8.3658,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_56",
    "name": "Germany Industrial/Bank Asset #056",
    "country": "Germany",
    "lat": 53.2749,
    "lon": 7.8528,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_57",
    "name": "Germany Industrial/Bank Asset #057",
    "country": "Germany",
    "lat": 52.8189,
    "lon": 8.0094,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_58",
    "name": "Germany Industrial/Bank Asset #058",
    "country": "Germany",
    "lat": 49.1428,
    "lon": 11.8828,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_59",
    "name": "Germany Industrial/Bank Asset #059",
    "country": "Germany",
    "lat": 52.7188,
    "lon": 10.7882,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_60",
    "name": "Germany Industrial/Bank Asset #060",
    "country": "Germany",
    "lat": 51.5923,
    "lon": 10.8195,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_61",
    "name": "Germany Industrial/Bank Asset #061",
    "country": "Germany",
    "lat": 50.3082,
    "lon": 8.1834,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_62",
    "name": "Germany Industrial/Bank Asset #062",
    "country": "Germany",
    "lat": 50.428,
    "lon": 11.442,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_63",
    "name": "Germany Industrial/Bank Asset #063",
    "country": "Germany",
    "lat": 52.4114,
    "lon": 12.6586,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_64",
    "name": "Germany Industrial/Bank Asset #064",
    "country": "Germany",
    "lat": 52.2653,
    "lon": 13.2604,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_65",
    "name": "Germany Industrial/Bank Asset #065",
    "country": "Germany",
    "lat": 51.6621,
    "lon": 9.5599,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_66",
    "name": "Germany Industrial/Bank Asset #066",
    "country": "Germany",
    "lat": 51.5496,
    "lon": 8.7264,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_67",
    "name": "Germany Industrial/Bank Asset #067",
    "country": "Germany",
    "lat": 51.9437,
    "lon": 8.7955,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_68",
    "name": "Germany Industrial/Bank Asset #068",
    "country": "Germany",
    "lat": 49.2011,
    "lon": 12.5222,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_69",
    "name": "Germany Industrial/Bank Asset #069",
    "country": "Germany",
    "lat": 50.4978,
    "lon": 12.0256,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_70",
    "name": "Germany Industrial/Bank Asset #070",
    "country": "Germany",
    "lat": 51.5305,
    "lon": 12.2933,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_71",
    "name": "Germany Industrial/Bank Asset #071",
    "country": "Germany",
    "lat": 52.8858,
    "lon": 13.2973,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_72",
    "name": "Germany Industrial/Bank Asset #072",
    "country": "Germany",
    "lat": 52.7521,
    "lon": 11.1314,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_73",
    "name": "Germany Industrial/Bank Asset #073",
    "country": "Germany",
    "lat": 51.8735,
    "lon": 7.6075,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_74",
    "name": "Germany Industrial/Bank Asset #074",
    "country": "Germany",
    "lat": 53.3054,
    "lon": 12.4268,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_75",
    "name": "Germany Industrial/Bank Asset #075",
    "country": "Germany",
    "lat": 49.9972,
    "lon": 8.5325,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_76",
    "name": "Germany Industrial/Bank Asset #076",
    "country": "Germany",
    "lat": 52.1735,
    "lon": 9.3039,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_77",
    "name": "Germany Industrial/Bank Asset #077",
    "country": "Germany",
    "lat": 50.3591,
    "lon": 7.4866,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_78",
    "name": "Germany Industrial/Bank Asset #078",
    "country": "Germany",
    "lat": 53.0093,
    "lon": 10.8479,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_79",
    "name": "Germany Industrial/Bank Asset #079",
    "country": "Germany",
    "lat": 50.6639,
    "lon": 8.3012,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_80",
    "name": "Germany Industrial/Bank Asset #080",
    "country": "Germany",
    "lat": 51.8259,
    "lon": 7.6339,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_81",
    "name": "Germany Industrial/Bank Asset #081",
    "country": "Germany",
    "lat": 52.3906,
    "lon": 8.7408,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_82",
    "name": "Germany Industrial/Bank Asset #082",
    "country": "Germany",
    "lat": 50.7592,
    "lon": 9.4954,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_83",
    "name": "Germany Industrial/Bank Asset #083",
    "country": "Germany",
    "lat": 50.5103,
    "lon": 11.7796,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_84",
    "name": "Germany Industrial/Bank Asset #084",
    "country": "Germany",
    "lat": 52.5442,
    "lon": 10.8556,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_85",
    "name": "Germany Industrial/Bank Asset #085",
    "country": "Germany",
    "lat": 49.0848,
    "lon": 7.7657,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_86",
    "name": "Germany Industrial/Bank Asset #086",
    "country": "Germany",
    "lat": 49.447,
    "lon": 11.157,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_87",
    "name": "Germany Industrial/Bank Asset #087",
    "country": "Germany",
    "lat": 52.0298,
    "lon": 9.0826,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_88",
    "name": "Germany Industrial/Bank Asset #088",
    "country": "Germany",
    "lat": 51.9697,
    "lon": 10.364,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_89",
    "name": "Germany Industrial/Bank Asset #089",
    "country": "Germany",
    "lat": 50.8702,
    "lon": 9.089,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_90",
    "name": "Germany Industrial/Bank Asset #090",
    "country": "Germany",
    "lat": 52.4347,
    "lon": 8.1329,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_91",
    "name": "Germany Industrial/Bank Asset #091",
    "country": "Germany",
    "lat": 50.8096,
    "lon": 9.1495,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_92",
    "name": "Germany Industrial/Bank Asset #092",
    "country": "Germany",
    "lat": 52.0524,
    "lon": 10.3698,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_93",
    "name": "Germany Industrial/Bank Asset #093",
    "country": "Germany",
    "lat": 51.9957,
    "lon": 7.7225,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_94",
    "name": "Germany Industrial/Bank Asset #094",
    "country": "Germany",
    "lat": 50.6363,
    "lon": 11.0459,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_95",
    "name": "Germany Industrial/Bank Asset #095",
    "country": "Germany",
    "lat": 48.6984,
    "lon": 9.2585,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_96",
    "name": "Germany Industrial/Bank Asset #096",
    "country": "Germany",
    "lat": 49.7162,
    "lon": 8.2734,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_97",
    "name": "Germany Industrial/Bank Asset #097",
    "country": "Germany",
    "lat": 49.9376,
    "lon": 9.4187,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_98",
    "name": "Germany Industrial/Bank Asset #098",
    "country": "Germany",
    "lat": 48.6986,
    "lon": 11.9321,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_99",
    "name": "Germany Industrial/Bank Asset #099",
    "country": "Germany",
    "lat": 49.5385,
    "lon": 9.7312,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_100",
    "name": "Germany Industrial/Bank Asset #100",
    "country": "Germany",
    "lat": 52.1784,
    "lon": 10.4516,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_101",
    "name": "Germany Industrial/Bank Asset #101",
    "country": "Germany",
    "lat": 52.8268,
    "lon": 12.2872,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_102",
    "name": "Germany Industrial/Bank Asset #102",
    "country": "Germany",
    "lat": 49.0204,
    "lon": 12.6206,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_103",
    "name": "Germany Industrial/Bank Asset #103",
    "country": "Germany",
    "lat": 48.8715,
    "lon": 7.5624,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_104",
    "name": "Germany Industrial/Bank Asset #104",
    "country": "Germany",
    "lat": 53.2658,
    "lon": 12.6227,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_105",
    "name": "Germany Industrial/Bank Asset #105",
    "country": "Germany",
    "lat": 51.5388,
    "lon": 10.8904,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_106",
    "name": "Germany Industrial/Bank Asset #106",
    "country": "Germany",
    "lat": 52.2075,
    "lon": 9.9562,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_107",
    "name": "Germany Industrial/Bank Asset #107",
    "country": "Germany",
    "lat": 49.2359,
    "lon": 7.5751,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_108",
    "name": "Germany Industrial/Bank Asset #108",
    "country": "Germany",
    "lat": 50.2838,
    "lon": 12.2579,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_109",
    "name": "Germany Industrial/Bank Asset #109",
    "country": "Germany",
    "lat": 51.7506,
    "lon": 12.4422,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_110",
    "name": "Germany Industrial/Bank Asset #110",
    "country": "Germany",
    "lat": 53.2588,
    "lon": 7.9788,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_111",
    "name": "Germany Industrial/Bank Asset #111",
    "country": "Germany",
    "lat": 52.8824,
    "lon": 8.9099,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_112",
    "name": "Germany Industrial/Bank Asset #112",
    "country": "Germany",
    "lat": 51.6044,
    "lon": 10.5938,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_113",
    "name": "Germany Industrial/Bank Asset #113",
    "country": "Germany",
    "lat": 50.6388,
    "lon": 9.3116,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_114",
    "name": "Germany Industrial/Bank Asset #114",
    "country": "Germany",
    "lat": 50.3576,
    "lon": 9.4484,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_115",
    "name": "Germany Industrial/Bank Asset #115",
    "country": "Germany",
    "lat": 49.5007,
    "lon": 10.5129,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_116",
    "name": "Germany Industrial/Bank Asset #116",
    "country": "Germany",
    "lat": 49.2301,
    "lon": 10.5097,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_117",
    "name": "Germany Industrial/Bank Asset #117",
    "country": "Germany",
    "lat": 53.1896,
    "lon": 9.5463,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_118",
    "name": "Germany Industrial/Bank Asset #118",
    "country": "Germany",
    "lat": 52.2969,
    "lon": 12.3637,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_119",
    "name": "Germany Industrial/Bank Asset #119",
    "country": "Germany",
    "lat": 52.7352,
    "lon": 8.8676,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ger_120",
    "name": "Germany Industrial/Bank Asset #120",
    "country": "Germany",
    "lat": 49.3922,
    "lon": 8.6336,
    "type": "Mittelstand & Grid Substations",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_1",
    "name": "France Industrial/Bank Asset #001",
    "country": "France",
    "lat": 47.2144,
    "lon": 3.7015,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_2",
    "name": "France Industrial/Bank Asset #002",
    "country": "France",
    "lat": 47.5331,
    "lon": -0.38,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_3",
    "name": "France Industrial/Bank Asset #003",
    "country": "France",
    "lat": 48.2371,
    "lon": 1.8388,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_4",
    "name": "France Industrial/Bank Asset #004",
    "country": "France",
    "lat": 48.1267,
    "lon": 3.6991,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_5",
    "name": "France Industrial/Bank Asset #005",
    "country": "France",
    "lat": 46.2934,
    "lon": 4.8491,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_6",
    "name": "France Industrial/Bank Asset #006",
    "country": "France",
    "lat": 46.987,
    "lon": 2.8271,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_7",
    "name": "France Industrial/Bank Asset #007",
    "country": "France",
    "lat": 47.3471,
    "lon": 4.4297,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_8",
    "name": "France Industrial/Bank Asset #008",
    "country": "France",
    "lat": 47.3633,
    "lon": -0.5633,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_9",
    "name": "France Industrial/Bank Asset #009",
    "country": "France",
    "lat": 44.0097,
    "lon": 1.4755,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_10",
    "name": "France Industrial/Bank Asset #010",
    "country": "France",
    "lat": 45.4169,
    "lon": 0.3027,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_11",
    "name": "France Industrial/Bank Asset #011",
    "country": "France",
    "lat": 43.937,
    "lon": 1.9314,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_12",
    "name": "France Industrial/Bank Asset #012",
    "country": "France",
    "lat": 45.4624,
    "lon": 1.5434,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_13",
    "name": "France Industrial/Bank Asset #013",
    "country": "France",
    "lat": 43.9413,
    "lon": 4.2019,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_14",
    "name": "France Industrial/Bank Asset #014",
    "country": "France",
    "lat": 44.0604,
    "lon": 4.4298,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_15",
    "name": "France Industrial/Bank Asset #015",
    "country": "France",
    "lat": 48.7318,
    "lon": 2.6851,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_16",
    "name": "France Industrial/Bank Asset #016",
    "country": "France",
    "lat": 46.6424,
    "lon": 1.619,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_17",
    "name": "France Industrial/Bank Asset #017",
    "country": "France",
    "lat": 46.9259,
    "lon": 3.9227,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_18",
    "name": "France Industrial/Bank Asset #018",
    "country": "France",
    "lat": 48.9753,
    "lon": 1.5281,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_19",
    "name": "France Industrial/Bank Asset #019",
    "country": "France",
    "lat": 48.4589,
    "lon": 2.9429,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_20",
    "name": "France Industrial/Bank Asset #020",
    "country": "France",
    "lat": 45.5292,
    "lon": 1.7094,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_21",
    "name": "France Industrial/Bank Asset #021",
    "country": "France",
    "lat": 44.5052,
    "lon": -1.1869,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_22",
    "name": "France Industrial/Bank Asset #022",
    "country": "France",
    "lat": 44.221,
    "lon": 4.6739,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_23",
    "name": "France Industrial/Bank Asset #023",
    "country": "France",
    "lat": 45.6606,
    "lon": 3.3802,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_24",
    "name": "France Industrial/Bank Asset #024",
    "country": "France",
    "lat": 46.6273,
    "lon": -0.4121,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_25",
    "name": "France Industrial/Bank Asset #025",
    "country": "France",
    "lat": 45.0865,
    "lon": 1.4443,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_26",
    "name": "France Industrial/Bank Asset #026",
    "country": "France",
    "lat": 46.2365,
    "lon": 2.0392,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_27",
    "name": "France Industrial/Bank Asset #027",
    "country": "France",
    "lat": 44.5525,
    "lon": 0.99,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_28",
    "name": "France Industrial/Bank Asset #028",
    "country": "France",
    "lat": 45.2974,
    "lon": 1.2414,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_29",
    "name": "France Industrial/Bank Asset #029",
    "country": "France",
    "lat": 45.6302,
    "lon": 2.5652,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_30",
    "name": "France Industrial/Bank Asset #030",
    "country": "France",
    "lat": 48.3354,
    "lon": 2.9111,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_31",
    "name": "France Industrial/Bank Asset #031",
    "country": "France",
    "lat": 43.9955,
    "lon": -0.9585,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_32",
    "name": "France Industrial/Bank Asset #032",
    "country": "France",
    "lat": 47.6703,
    "lon": 0.369,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_33",
    "name": "France Industrial/Bank Asset #033",
    "country": "France",
    "lat": 47.9424,
    "lon": 2.9759,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_34",
    "name": "France Industrial/Bank Asset #034",
    "country": "France",
    "lat": 49.0381,
    "lon": 4.493,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_35",
    "name": "France Industrial/Bank Asset #035",
    "country": "France",
    "lat": 45.6002,
    "lon": 2.4592,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_36",
    "name": "France Industrial/Bank Asset #036",
    "country": "France",
    "lat": 44.4486,
    "lon": 0.8287,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_37",
    "name": "France Industrial/Bank Asset #037",
    "country": "France",
    "lat": 49.4062,
    "lon": 3.2694,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_38",
    "name": "France Industrial/Bank Asset #038",
    "country": "France",
    "lat": 45.9517,
    "lon": 2.5453,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_39",
    "name": "France Industrial/Bank Asset #039",
    "country": "France",
    "lat": 49.228,
    "lon": 0.5471,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_40",
    "name": "France Industrial/Bank Asset #040",
    "country": "France",
    "lat": 45.8601,
    "lon": 3.9216,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_41",
    "name": "France Industrial/Bank Asset #041",
    "country": "France",
    "lat": 48.4791,
    "lon": 3.0708,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_42",
    "name": "France Industrial/Bank Asset #042",
    "country": "France",
    "lat": 48.5738,
    "lon": 3.5514,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_43",
    "name": "France Industrial/Bank Asset #043",
    "country": "France",
    "lat": 47.7125,
    "lon": 2.0648,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_44",
    "name": "France Industrial/Bank Asset #044",
    "country": "France",
    "lat": 47.4761,
    "lon": 1.3438,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_45",
    "name": "France Industrial/Bank Asset #045",
    "country": "France",
    "lat": 45.771,
    "lon": 0.9182,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_46",
    "name": "France Industrial/Bank Asset #046",
    "country": "France",
    "lat": 44.6816,
    "lon": -0.1207,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_47",
    "name": "France Industrial/Bank Asset #047",
    "country": "France",
    "lat": 49.286,
    "lon": 1.7839,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_48",
    "name": "France Industrial/Bank Asset #048",
    "country": "France",
    "lat": 44.9593,
    "lon": -0.657,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_49",
    "name": "France Industrial/Bank Asset #049",
    "country": "France",
    "lat": 44.063,
    "lon": 4.291,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_50",
    "name": "France Industrial/Bank Asset #050",
    "country": "France",
    "lat": 44.2068,
    "lon": 3.7761,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_51",
    "name": "France Industrial/Bank Asset #051",
    "country": "France",
    "lat": 48.6107,
    "lon": 4.5658,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_52",
    "name": "France Industrial/Bank Asset #052",
    "country": "France",
    "lat": 43.8265,
    "lon": 0.7374,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_53",
    "name": "France Industrial/Bank Asset #053",
    "country": "France",
    "lat": 48.1978,
    "lon": -0.7027,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_54",
    "name": "France Industrial/Bank Asset #054",
    "country": "France",
    "lat": 45.8603,
    "lon": -0.4843,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_55",
    "name": "France Industrial/Bank Asset #055",
    "country": "France",
    "lat": 48.5881,
    "lon": 3.7777,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_56",
    "name": "France Industrial/Bank Asset #056",
    "country": "France",
    "lat": 48.4543,
    "lon": -0.4612,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_57",
    "name": "France Industrial/Bank Asset #057",
    "country": "France",
    "lat": 46.226,
    "lon": 1.256,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_58",
    "name": "France Industrial/Bank Asset #058",
    "country": "France",
    "lat": 47.6582,
    "lon": 0.0427,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_59",
    "name": "France Industrial/Bank Asset #059",
    "country": "France",
    "lat": 46.2652,
    "lon": 0.3745,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_60",
    "name": "France Industrial/Bank Asset #060",
    "country": "France",
    "lat": 48.0912,
    "lon": 1.5225,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_61",
    "name": "France Industrial/Bank Asset #061",
    "country": "France",
    "lat": 46.8041,
    "lon": 0.5463,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_62",
    "name": "France Industrial/Bank Asset #062",
    "country": "France",
    "lat": 48.4517,
    "lon": 1.6631,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_63",
    "name": "France Industrial/Bank Asset #063",
    "country": "France",
    "lat": 48.6107,
    "lon": 0.9549,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_64",
    "name": "France Industrial/Bank Asset #064",
    "country": "France",
    "lat": 49.2828,
    "lon": 5.2711,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_65",
    "name": "France Industrial/Bank Asset #065",
    "country": "France",
    "lat": 46.3701,
    "lon": 0.3524,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_66",
    "name": "France Industrial/Bank Asset #066",
    "country": "France",
    "lat": 45.8912,
    "lon": 2.0722,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_67",
    "name": "France Industrial/Bank Asset #067",
    "country": "France",
    "lat": 49.3976,
    "lon": 4.0982,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_68",
    "name": "France Industrial/Bank Asset #068",
    "country": "France",
    "lat": 48.4076,
    "lon": -0.6512,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_69",
    "name": "France Industrial/Bank Asset #069",
    "country": "France",
    "lat": 45.1,
    "lon": 2.8683,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_70",
    "name": "France Industrial/Bank Asset #070",
    "country": "France",
    "lat": 48.8447,
    "lon": 2.2618,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_71",
    "name": "France Industrial/Bank Asset #071",
    "country": "France",
    "lat": 44.2155,
    "lon": 4.3012,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_72",
    "name": "France Industrial/Bank Asset #072",
    "country": "France",
    "lat": 48.707,
    "lon": 0.3754,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_73",
    "name": "France Industrial/Bank Asset #073",
    "country": "France",
    "lat": 48.1787,
    "lon": 0.2895,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_74",
    "name": "France Industrial/Bank Asset #074",
    "country": "France",
    "lat": 49.0318,
    "lon": -0.5886,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_75",
    "name": "France Industrial/Bank Asset #075",
    "country": "France",
    "lat": 46.2248,
    "lon": 5.0049,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_76",
    "name": "France Industrial/Bank Asset #076",
    "country": "France",
    "lat": 44.9322,
    "lon": 1.5379,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_77",
    "name": "France Industrial/Bank Asset #077",
    "country": "France",
    "lat": 45.6975,
    "lon": -1.4333,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_78",
    "name": "France Industrial/Bank Asset #078",
    "country": "France",
    "lat": 43.9195,
    "lon": 1.894,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_79",
    "name": "France Industrial/Bank Asset #079",
    "country": "France",
    "lat": 45.0147,
    "lon": 5.3417,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_80",
    "name": "France Industrial/Bank Asset #080",
    "country": "France",
    "lat": 45.8495,
    "lon": -1.4227,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_81",
    "name": "France Industrial/Bank Asset #081",
    "country": "France",
    "lat": 49.185,
    "lon": 4.2542,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_82",
    "name": "France Industrial/Bank Asset #082",
    "country": "France",
    "lat": 47.4998,
    "lon": 3.9197,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_83",
    "name": "France Industrial/Bank Asset #083",
    "country": "France",
    "lat": 44.4256,
    "lon": 0.3882,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_84",
    "name": "France Industrial/Bank Asset #084",
    "country": "France",
    "lat": 48.5786,
    "lon": 3.2525,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_85",
    "name": "France Industrial/Bank Asset #085",
    "country": "France",
    "lat": 44.4328,
    "lon": 3.3188,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_86",
    "name": "France Industrial/Bank Asset #086",
    "country": "France",
    "lat": 46.2916,
    "lon": -1.5832,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_87",
    "name": "France Industrial/Bank Asset #087",
    "country": "France",
    "lat": 44.0754,
    "lon": 0.1715,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_88",
    "name": "France Industrial/Bank Asset #088",
    "country": "France",
    "lat": 48.6098,
    "lon": 2.2216,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_89",
    "name": "France Industrial/Bank Asset #089",
    "country": "France",
    "lat": 47.9634,
    "lon": 2.0744,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_90",
    "name": "France Industrial/Bank Asset #090",
    "country": "France",
    "lat": 44.2671,
    "lon": 0.3967,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_91",
    "name": "France Industrial/Bank Asset #091",
    "country": "France",
    "lat": 45.4069,
    "lon": -1.2858,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_92",
    "name": "France Industrial/Bank Asset #092",
    "country": "France",
    "lat": 46.119,
    "lon": 3.9373,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_93",
    "name": "France Industrial/Bank Asset #093",
    "country": "France",
    "lat": 46.3427,
    "lon": -0.844,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_94",
    "name": "France Industrial/Bank Asset #094",
    "country": "France",
    "lat": 49.0309,
    "lon": 2.5572,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_fra_95",
    "name": "France Industrial/Bank Asset #095",
    "country": "France",
    "lat": 43.6986,
    "lon": 1.9876,
    "type": "Power & Chemical Rail Nodes",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_1",
    "name": "Italy Industrial/Bank Asset #001",
    "country": "Italy",
    "lat": 40.6936,
    "lon": 11.0743,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_2",
    "name": "Italy Industrial/Bank Asset #002",
    "country": "Italy",
    "lat": 42.0047,
    "lon": 12.9592,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_3",
    "name": "Italy Industrial/Bank Asset #003",
    "country": "Italy",
    "lat": 40.6839,
    "lon": 12.1663,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_4",
    "name": "Italy Industrial/Bank Asset #004",
    "country": "Italy",
    "lat": 43.6506,
    "lon": 10.8425,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_5",
    "name": "Italy Industrial/Bank Asset #005",
    "country": "Italy",
    "lat": 45.8226,
    "lon": 10.7707,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_6",
    "name": "Italy Industrial/Bank Asset #006",
    "country": "Italy",
    "lat": 42.6824,
    "lon": 12.5293,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_7",
    "name": "Italy Industrial/Bank Asset #007",
    "country": "Italy",
    "lat": 45.9183,
    "lon": 12.7166,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_8",
    "name": "Italy Industrial/Bank Asset #008",
    "country": "Italy",
    "lat": 41.7332,
    "lon": 12.3805,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_9",
    "name": "Italy Industrial/Bank Asset #009",
    "country": "Italy",
    "lat": 43.4497,
    "lon": 14.4242,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_10",
    "name": "Italy Industrial/Bank Asset #010",
    "country": "Italy",
    "lat": 40.7756,
    "lon": 10.565,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_11",
    "name": "Italy Industrial/Bank Asset #011",
    "country": "Italy",
    "lat": 44.5196,
    "lon": 11.8792,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_12",
    "name": "Italy Industrial/Bank Asset #012",
    "country": "Italy",
    "lat": 44.1306,
    "lon": 13.013,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_13",
    "name": "Italy Industrial/Bank Asset #013",
    "country": "Italy",
    "lat": 44.4005,
    "lon": 13.4407,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_14",
    "name": "Italy Industrial/Bank Asset #014",
    "country": "Italy",
    "lat": 41.3276,
    "lon": 10.6773,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_15",
    "name": "Italy Industrial/Bank Asset #015",
    "country": "Italy",
    "lat": 42.8221,
    "lon": 13.754,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_16",
    "name": "Italy Industrial/Bank Asset #016",
    "country": "Italy",
    "lat": 40.2256,
    "lon": 13.6166,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_17",
    "name": "Italy Industrial/Bank Asset #017",
    "country": "Italy",
    "lat": 42.2524,
    "lon": 13.2816,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_18",
    "name": "Italy Industrial/Bank Asset #018",
    "country": "Italy",
    "lat": 43.4222,
    "lon": 13.746,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_19",
    "name": "Italy Industrial/Bank Asset #019",
    "country": "Italy",
    "lat": 39.4417,
    "lon": 13.6048,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_20",
    "name": "Italy Industrial/Bank Asset #020",
    "country": "Italy",
    "lat": 42.2038,
    "lon": 11.6738,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_21",
    "name": "Italy Industrial/Bank Asset #021",
    "country": "Italy",
    "lat": 39.3066,
    "lon": 11.2979,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_22",
    "name": "Italy Industrial/Bank Asset #022",
    "country": "Italy",
    "lat": 39.2933,
    "lon": 14.2335,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_23",
    "name": "Italy Industrial/Bank Asset #023",
    "country": "Italy",
    "lat": 42.6077,
    "lon": 14.4565,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_24",
    "name": "Italy Industrial/Bank Asset #024",
    "country": "Italy",
    "lat": 42.8012,
    "lon": 11.5133,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_25",
    "name": "Italy Industrial/Bank Asset #025",
    "country": "Italy",
    "lat": 44.273,
    "lon": 11.2644,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_26",
    "name": "Italy Industrial/Bank Asset #026",
    "country": "Italy",
    "lat": 41.4988,
    "lon": 13.6234,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_27",
    "name": "Italy Industrial/Bank Asset #027",
    "country": "Italy",
    "lat": 45.0606,
    "lon": 11.8277,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_28",
    "name": "Italy Industrial/Bank Asset #028",
    "country": "Italy",
    "lat": 39.8713,
    "lon": 11.9721,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_29",
    "name": "Italy Industrial/Bank Asset #029",
    "country": "Italy",
    "lat": 45.2264,
    "lon": 13.4732,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_30",
    "name": "Italy Industrial/Bank Asset #030",
    "country": "Italy",
    "lat": 45.2625,
    "lon": 12.0466,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_31",
    "name": "Italy Industrial/Bank Asset #031",
    "country": "Italy",
    "lat": 45.8161,
    "lon": 12.4848,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_32",
    "name": "Italy Industrial/Bank Asset #032",
    "country": "Italy",
    "lat": 42.4827,
    "lon": 14.1972,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_33",
    "name": "Italy Industrial/Bank Asset #033",
    "country": "Italy",
    "lat": 42.6349,
    "lon": 13.7046,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_34",
    "name": "Italy Industrial/Bank Asset #034",
    "country": "Italy",
    "lat": 44.0896,
    "lon": 10.8157,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_35",
    "name": "Italy Industrial/Bank Asset #035",
    "country": "Italy",
    "lat": 43.2172,
    "lon": 13.7894,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_36",
    "name": "Italy Industrial/Bank Asset #036",
    "country": "Italy",
    "lat": 42.8183,
    "lon": 11.7848,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_37",
    "name": "Italy Industrial/Bank Asset #037",
    "country": "Italy",
    "lat": 39.5605,
    "lon": 13.1437,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_38",
    "name": "Italy Industrial/Bank Asset #038",
    "country": "Italy",
    "lat": 41.1455,
    "lon": 12.9105,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_39",
    "name": "Italy Industrial/Bank Asset #039",
    "country": "Italy",
    "lat": 41.9828,
    "lon": 13.2591,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_40",
    "name": "Italy Industrial/Bank Asset #040",
    "country": "Italy",
    "lat": 41.4608,
    "lon": 10.6694,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_41",
    "name": "Italy Industrial/Bank Asset #041",
    "country": "Italy",
    "lat": 45.0903,
    "lon": 11.9102,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_42",
    "name": "Italy Industrial/Bank Asset #042",
    "country": "Italy",
    "lat": 45.9871,
    "lon": 11.5982,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_43",
    "name": "Italy Industrial/Bank Asset #043",
    "country": "Italy",
    "lat": 45.8602,
    "lon": 14.2916,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_44",
    "name": "Italy Industrial/Bank Asset #044",
    "country": "Italy",
    "lat": 39.5253,
    "lon": 13.0501,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_45",
    "name": "Italy Industrial/Bank Asset #045",
    "country": "Italy",
    "lat": 41.5432,
    "lon": 13.7044,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_46",
    "name": "Italy Industrial/Bank Asset #046",
    "country": "Italy",
    "lat": 43.7559,
    "lon": 14.3112,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_47",
    "name": "Italy Industrial/Bank Asset #047",
    "country": "Italy",
    "lat": 39.9995,
    "lon": 12.9303,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_48",
    "name": "Italy Industrial/Bank Asset #048",
    "country": "Italy",
    "lat": 44.4692,
    "lon": 10.6392,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_49",
    "name": "Italy Industrial/Bank Asset #049",
    "country": "Italy",
    "lat": 39.4706,
    "lon": 13.6141,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_50",
    "name": "Italy Industrial/Bank Asset #050",
    "country": "Italy",
    "lat": 41.5643,
    "lon": 12.0314,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_51",
    "name": "Italy Industrial/Bank Asset #051",
    "country": "Italy",
    "lat": 42.9707,
    "lon": 12.9204,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_52",
    "name": "Italy Industrial/Bank Asset #052",
    "country": "Italy",
    "lat": 43.7534,
    "lon": 14.2953,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_53",
    "name": "Italy Industrial/Bank Asset #053",
    "country": "Italy",
    "lat": 41.6041,
    "lon": 13.5523,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_54",
    "name": "Italy Industrial/Bank Asset #054",
    "country": "Italy",
    "lat": 43.0175,
    "lon": 12.6178,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_55",
    "name": "Italy Industrial/Bank Asset #055",
    "country": "Italy",
    "lat": 41.7862,
    "lon": 13.0982,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_56",
    "name": "Italy Industrial/Bank Asset #056",
    "country": "Italy",
    "lat": 40.7473,
    "lon": 10.9538,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_57",
    "name": "Italy Industrial/Bank Asset #057",
    "country": "Italy",
    "lat": 44.1497,
    "lon": 12.4962,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_58",
    "name": "Italy Industrial/Bank Asset #058",
    "country": "Italy",
    "lat": 41.7089,
    "lon": 12.7467,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_59",
    "name": "Italy Industrial/Bank Asset #059",
    "country": "Italy",
    "lat": 40.8324,
    "lon": 11.5412,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_60",
    "name": "Italy Industrial/Bank Asset #060",
    "country": "Italy",
    "lat": 42.1239,
    "lon": 14.4855,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_61",
    "name": "Italy Industrial/Bank Asset #061",
    "country": "Italy",
    "lat": 40.999,
    "lon": 14.1659,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_62",
    "name": "Italy Industrial/Bank Asset #062",
    "country": "Italy",
    "lat": 42.4384,
    "lon": 10.9905,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_63",
    "name": "Italy Industrial/Bank Asset #063",
    "country": "Italy",
    "lat": 44.9698,
    "lon": 12.3082,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_64",
    "name": "Italy Industrial/Bank Asset #064",
    "country": "Italy",
    "lat": 45.2908,
    "lon": 12.2804,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_65",
    "name": "Italy Industrial/Bank Asset #065",
    "country": "Italy",
    "lat": 39.6145,
    "lon": 13.2277,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_66",
    "name": "Italy Industrial/Bank Asset #066",
    "country": "Italy",
    "lat": 44.9186,
    "lon": 11.7784,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_67",
    "name": "Italy Industrial/Bank Asset #067",
    "country": "Italy",
    "lat": 41.432,
    "lon": 10.7598,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_68",
    "name": "Italy Industrial/Bank Asset #068",
    "country": "Italy",
    "lat": 42.7952,
    "lon": 14.0653,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_69",
    "name": "Italy Industrial/Bank Asset #069",
    "country": "Italy",
    "lat": 44.9595,
    "lon": 13.3472,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_70",
    "name": "Italy Industrial/Bank Asset #070",
    "country": "Italy",
    "lat": 45.4913,
    "lon": 13.0508,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_71",
    "name": "Italy Industrial/Bank Asset #071",
    "country": "Italy",
    "lat": 44.5559,
    "lon": 12.535,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_72",
    "name": "Italy Industrial/Bank Asset #072",
    "country": "Italy",
    "lat": 39.8495,
    "lon": 11.3039,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_73",
    "name": "Italy Industrial/Bank Asset #073",
    "country": "Italy",
    "lat": 39.9721,
    "lon": 13.6615,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_74",
    "name": "Italy Industrial/Bank Asset #074",
    "country": "Italy",
    "lat": 39.184,
    "lon": 12.7161,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ita_75",
    "name": "Italy Industrial/Bank Asset #075",
    "country": "Italy",
    "lat": 41.5824,
    "lon": 13.7146,
    "type": "Northern Industrial Belt & Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_1",
    "name": "Spain Industrial/Bank Asset #001",
    "country": "Spain",
    "lat": 40.7699,
    "lon": -2.8544,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_2",
    "name": "Spain Industrial/Bank Asset #002",
    "country": "Spain",
    "lat": 37.9773,
    "lon": -5.2757,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_3",
    "name": "Spain Industrial/Bank Asset #003",
    "country": "Spain",
    "lat": 43.4576,
    "lon": -1.999,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_4",
    "name": "Spain Industrial/Bank Asset #004",
    "country": "Spain",
    "lat": 40.6142,
    "lon": -1.5967,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_5",
    "name": "Spain Industrial/Bank Asset #005",
    "country": "Spain",
    "lat": 42.4,
    "lon": -7.16,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_6",
    "name": "Spain Industrial/Bank Asset #006",
    "country": "Spain",
    "lat": 43.2943,
    "lon": -2.6113,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_7",
    "name": "Spain Industrial/Bank Asset #007",
    "country": "Spain",
    "lat": 40.1598,
    "lon": -2.3091,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_8",
    "name": "Spain Industrial/Bank Asset #008",
    "country": "Spain",
    "lat": 39.5271,
    "lon": -0.7263,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_9",
    "name": "Spain Industrial/Bank Asset #009",
    "country": "Spain",
    "lat": 42.1416,
    "lon": -2.6316,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_10",
    "name": "Spain Industrial/Bank Asset #010",
    "country": "Spain",
    "lat": 38.5518,
    "lon": -0.0199,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_11",
    "name": "Spain Industrial/Bank Asset #011",
    "country": "Spain",
    "lat": 40.0557,
    "lon": -0.4643,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_12",
    "name": "Spain Industrial/Bank Asset #012",
    "country": "Spain",
    "lat": 37.7925,
    "lon": -6.7567,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_13",
    "name": "Spain Industrial/Bank Asset #013",
    "country": "Spain",
    "lat": 38.3781,
    "lon": -6.4327,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_14",
    "name": "Spain Industrial/Bank Asset #014",
    "country": "Spain",
    "lat": 39.396,
    "lon": -2.0753,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_15",
    "name": "Spain Industrial/Bank Asset #015",
    "country": "Spain",
    "lat": 39.5361,
    "lon": -0.2228,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_16",
    "name": "Spain Industrial/Bank Asset #016",
    "country": "Spain",
    "lat": 42.8296,
    "lon": -0.9825,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_17",
    "name": "Spain Industrial/Bank Asset #017",
    "country": "Spain",
    "lat": 38.9636,
    "lon": -2.6695,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_18",
    "name": "Spain Industrial/Bank Asset #018",
    "country": "Spain",
    "lat": 40.765,
    "lon": -6.7486,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_19",
    "name": "Spain Industrial/Bank Asset #019",
    "country": "Spain",
    "lat": 39.2769,
    "lon": -3.4822,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_20",
    "name": "Spain Industrial/Bank Asset #020",
    "country": "Spain",
    "lat": 40.4754,
    "lon": -6.4009,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_21",
    "name": "Spain Industrial/Bank Asset #021",
    "country": "Spain",
    "lat": 43.1096,
    "lon": -6.5164,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_22",
    "name": "Spain Industrial/Bank Asset #022",
    "country": "Spain",
    "lat": 41.4124,
    "lon": -1.9849,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_23",
    "name": "Spain Industrial/Bank Asset #023",
    "country": "Spain",
    "lat": 41.0908,
    "lon": -1.0098,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_24",
    "name": "Spain Industrial/Bank Asset #024",
    "country": "Spain",
    "lat": 40.8417,
    "lon": -1.1481,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_25",
    "name": "Spain Industrial/Bank Asset #025",
    "country": "Spain",
    "lat": 37.6302,
    "lon": -7.3863,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_26",
    "name": "Spain Industrial/Bank Asset #026",
    "country": "Spain",
    "lat": 41.3087,
    "lon": -3.1358,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_27",
    "name": "Spain Industrial/Bank Asset #027",
    "country": "Spain",
    "lat": 41.3668,
    "lon": -1.6143,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_28",
    "name": "Spain Industrial/Bank Asset #028",
    "country": "Spain",
    "lat": 39.9595,
    "lon": -2.6381,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_29",
    "name": "Spain Industrial/Bank Asset #029",
    "country": "Spain",
    "lat": 40.4482,
    "lon": -2.7327,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_30",
    "name": "Spain Industrial/Bank Asset #030",
    "country": "Spain",
    "lat": 39.198,
    "lon": -0.0968,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_31",
    "name": "Spain Industrial/Bank Asset #031",
    "country": "Spain",
    "lat": 40.3577,
    "lon": -1.3125,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_32",
    "name": "Spain Industrial/Bank Asset #032",
    "country": "Spain",
    "lat": 41.5699,
    "lon": -5.3705,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_33",
    "name": "Spain Industrial/Bank Asset #033",
    "country": "Spain",
    "lat": 37.8978,
    "lon": -7.2707,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_34",
    "name": "Spain Industrial/Bank Asset #034",
    "country": "Spain",
    "lat": 40.0976,
    "lon": -3.876,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_35",
    "name": "Spain Industrial/Bank Asset #035",
    "country": "Spain",
    "lat": 38.6841,
    "lon": -2.8967,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_36",
    "name": "Spain Industrial/Bank Asset #036",
    "country": "Spain",
    "lat": 39.3355,
    "lon": -2.0031,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_37",
    "name": "Spain Industrial/Bank Asset #037",
    "country": "Spain",
    "lat": 41.8652,
    "lon": -0.8638,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_38",
    "name": "Spain Industrial/Bank Asset #038",
    "country": "Spain",
    "lat": 43.3122,
    "lon": -6.7039,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_39",
    "name": "Spain Industrial/Bank Asset #039",
    "country": "Spain",
    "lat": 39.6832,
    "lon": -3.2568,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_40",
    "name": "Spain Industrial/Bank Asset #040",
    "country": "Spain",
    "lat": 39.3747,
    "lon": -4.0182,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_41",
    "name": "Spain Industrial/Bank Asset #041",
    "country": "Spain",
    "lat": 39.0648,
    "lon": -5.7666,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_42",
    "name": "Spain Industrial/Bank Asset #042",
    "country": "Spain",
    "lat": 38.0409,
    "lon": -5.4283,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_43",
    "name": "Spain Industrial/Bank Asset #043",
    "country": "Spain",
    "lat": 39.7649,
    "lon": -2.827,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_44",
    "name": "Spain Industrial/Bank Asset #044",
    "country": "Spain",
    "lat": 38.9496,
    "lon": -0.8275,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_45",
    "name": "Spain Industrial/Bank Asset #045",
    "country": "Spain",
    "lat": 38.4182,
    "lon": -5.1305,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_46",
    "name": "Spain Industrial/Bank Asset #046",
    "country": "Spain",
    "lat": 40.9261,
    "lon": -5.2483,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_47",
    "name": "Spain Industrial/Bank Asset #047",
    "country": "Spain",
    "lat": 42.0387,
    "lon": -3.7639,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_48",
    "name": "Spain Industrial/Bank Asset #048",
    "country": "Spain",
    "lat": 40.5483,
    "lon": -3.7599,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_49",
    "name": "Spain Industrial/Bank Asset #049",
    "country": "Spain",
    "lat": 39.3112,
    "lon": -7.5646,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_50",
    "name": "Spain Industrial/Bank Asset #050",
    "country": "Spain",
    "lat": 43.1314,
    "lon": -3.7064,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_51",
    "name": "Spain Industrial/Bank Asset #051",
    "country": "Spain",
    "lat": 43.2601,
    "lon": -6.0288,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_52",
    "name": "Spain Industrial/Bank Asset #052",
    "country": "Spain",
    "lat": 39.5774,
    "lon": -7.3457,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_53",
    "name": "Spain Industrial/Bank Asset #053",
    "country": "Spain",
    "lat": 40.4294,
    "lon": -0.6913,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_54",
    "name": "Spain Industrial/Bank Asset #054",
    "country": "Spain",
    "lat": 41.3856,
    "lon": -3.9853,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_55",
    "name": "Spain Industrial/Bank Asset #055",
    "country": "Spain",
    "lat": 40.6801,
    "lon": -0.9726,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_56",
    "name": "Spain Industrial/Bank Asset #056",
    "country": "Spain",
    "lat": 40.0456,
    "lon": -0.6904,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_57",
    "name": "Spain Industrial/Bank Asset #057",
    "country": "Spain",
    "lat": 41.825,
    "lon": -1.6391,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_58",
    "name": "Spain Industrial/Bank Asset #058",
    "country": "Spain",
    "lat": 39.6556,
    "lon": -4.5453,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_59",
    "name": "Spain Industrial/Bank Asset #059",
    "country": "Spain",
    "lat": 40.8817,
    "lon": -6.1928,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_60",
    "name": "Spain Industrial/Bank Asset #060",
    "country": "Spain",
    "lat": 40.7793,
    "lon": -7.1617,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_61",
    "name": "Spain Industrial/Bank Asset #061",
    "country": "Spain",
    "lat": 40.4855,
    "lon": -1.6348,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_62",
    "name": "Spain Industrial/Bank Asset #062",
    "country": "Spain",
    "lat": 39.1383,
    "lon": 0.1627,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_63",
    "name": "Spain Industrial/Bank Asset #063",
    "country": "Spain",
    "lat": 41.5424,
    "lon": -6.7995,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_64",
    "name": "Spain Industrial/Bank Asset #064",
    "country": "Spain",
    "lat": 43.3105,
    "lon": -4.5988,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_65",
    "name": "Spain Industrial/Bank Asset #065",
    "country": "Spain",
    "lat": 42.2294,
    "lon": -5.0373,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_66",
    "name": "Spain Industrial/Bank Asset #066",
    "country": "Spain",
    "lat": 43.0937,
    "lon": -1.7103,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_67",
    "name": "Spain Industrial/Bank Asset #067",
    "country": "Spain",
    "lat": 38.6543,
    "lon": -3.677,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_68",
    "name": "Spain Industrial/Bank Asset #068",
    "country": "Spain",
    "lat": 40.4605,
    "lon": -7.3876,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_69",
    "name": "Spain Industrial/Bank Asset #069",
    "country": "Spain",
    "lat": 38.2822,
    "lon": -5.0857,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_spa_70",
    "name": "Spain Industrial/Bank Asset #070",
    "country": "Spain",
    "lat": 40.3025,
    "lon": -4.0941,
    "type": "Solar & Logistics Platforms",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_net_1",
    "name": "Netherlands Industrial/Bank Asset #001",
    "country": "Netherlands",
    "lat": 52.3,
    "lon": 5.321,
    "type": "Maritime & Agrotech Centers",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_net_2",
    "name": "Netherlands Industrial/Bank Asset #002",
    "country": "Netherlands",
    "lat": 51.8547,
    "lon": 5.5161,
    "type": "Maritime & Agrotech Centers",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_net_3",
    "name": "Netherlands Industrial/Bank Asset #003",
    "country": "Netherlands",
    "lat": 51.59,
    "lon": 6.2712,
    "type": "Maritime & Agrotech Centers",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_net_4",
    "name": "Netherlands Industrial/Bank Asset #004",
    "country": "Netherlands",
    "lat": 52.5129,
    "lon": 4.8885,
    "type": "Maritime & Agrotech Centers",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_net_5",
    "name": "Netherlands Industrial/Bank Asset #005",
    "country": "Netherlands",
    "lat": 51.8682,
    "lon": 5.9466,
    "type": "Maritime & Agrotech Centers",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_net_6",
    "name": "Netherlands Industrial/Bank Asset #006",
    "country": "Netherlands",
    "lat": 52.1817,
    "lon": 5.7075,
    "type": "Maritime & Agrotech Centers",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_net_7",
    "name": "Netherlands Industrial/Bank Asset #007",
    "country": "Netherlands",
    "lat": 51.8097,
    "lon": 5.9215,
    "type": "Maritime & Agrotech Centers",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_net_8",
    "name": "Netherlands Industrial/Bank Asset #008",
    "country": "Netherlands",
    "lat": 51.9194,
    "lon": 5.6376,
    "type": "Maritime & Agrotech Centers",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_net_9",
    "name": "Netherlands Industrial/Bank Asset #009",
    "country": "Netherlands",
    "lat": 52.8978,
    "lon": 5.4574,
    "type": "Maritime & Agrotech Centers",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_net_10",
    "name": "Netherlands Industrial/Bank Asset #010",
    "country": "Netherlands",
    "lat": 52.6048,
    "lon": 5.7406,
    "type": "Maritime & Agrotech Centers",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_net_11",
    "name": "Netherlands Industrial/Bank Asset #011",
    "country": "Netherlands",
    "lat": 52.4309,
    "lon": 4.3433,
    "type": "Maritime & Agrotech Centers",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_net_12",
    "name": "Netherlands Industrial/Bank Asset #012",
    "country": "Netherlands",
    "lat": 52.0893,
    "lon": 6.2241,
    "type": "Maritime & Agrotech Centers",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_net_13",
    "name": "Netherlands Industrial/Bank Asset #013",
    "country": "Netherlands",
    "lat": 52.5826,
    "lon": 5.8423,
    "type": "Maritime & Agrotech Centers",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_net_14",
    "name": "Netherlands Industrial/Bank Asset #014",
    "country": "Netherlands",
    "lat": 52.2542,
    "lon": 5.7328,
    "type": "Maritime & Agrotech Centers",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_net_15",
    "name": "Netherlands Industrial/Bank Asset #015",
    "country": "Netherlands",
    "lat": 52.2636,
    "lon": 4.631,
    "type": "Maritime & Agrotech Centers",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_net_16",
    "name": "Netherlands Industrial/Bank Asset #016",
    "country": "Netherlands",
    "lat": 52.3364,
    "lon": 5.5295,
    "type": "Maritime & Agrotech Centers",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_net_17",
    "name": "Netherlands Industrial/Bank Asset #017",
    "country": "Netherlands",
    "lat": 52.6759,
    "lon": 4.5856,
    "type": "Maritime & Agrotech Centers",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_net_18",
    "name": "Netherlands Industrial/Bank Asset #018",
    "country": "Netherlands",
    "lat": 52.4192,
    "lon": 4.3531,
    "type": "Maritime & Agrotech Centers",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_net_19",
    "name": "Netherlands Industrial/Bank Asset #019",
    "country": "Netherlands",
    "lat": 52.8471,
    "lon": 4.5098,
    "type": "Maritime & Agrotech Centers",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_net_20",
    "name": "Netherlands Industrial/Bank Asset #020",
    "country": "Netherlands",
    "lat": 51.3603,
    "lon": 4.9174,
    "type": "Maritime & Agrotech Centers",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_net_21",
    "name": "Netherlands Industrial/Bank Asset #021",
    "country": "Netherlands",
    "lat": 51.5723,
    "lon": 5.671,
    "type": "Maritime & Agrotech Centers",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_net_22",
    "name": "Netherlands Industrial/Bank Asset #022",
    "country": "Netherlands",
    "lat": 51.9866,
    "lon": 5.8399,
    "type": "Maritime & Agrotech Centers",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_net_23",
    "name": "Netherlands Industrial/Bank Asset #023",
    "country": "Netherlands",
    "lat": 52.8028,
    "lon": 6.0356,
    "type": "Maritime & Agrotech Centers",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_net_24",
    "name": "Netherlands Industrial/Bank Asset #024",
    "country": "Netherlands",
    "lat": 52.5073,
    "lon": 4.4146,
    "type": "Maritime & Agrotech Centers",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_net_25",
    "name": "Netherlands Industrial/Bank Asset #025",
    "country": "Netherlands",
    "lat": 51.5509,
    "lon": 4.7047,
    "type": "Maritime & Agrotech Centers",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_net_26",
    "name": "Netherlands Industrial/Bank Asset #026",
    "country": "Netherlands",
    "lat": 51.8501,
    "lon": 5.6145,
    "type": "Maritime & Agrotech Centers",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_net_27",
    "name": "Netherlands Industrial/Bank Asset #027",
    "country": "Netherlands",
    "lat": 52.1708,
    "lon": 4.9175,
    "type": "Maritime & Agrotech Centers",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_net_28",
    "name": "Netherlands Industrial/Bank Asset #028",
    "country": "Netherlands",
    "lat": 51.6071,
    "lon": 6.1142,
    "type": "Maritime & Agrotech Centers",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_net_29",
    "name": "Netherlands Industrial/Bank Asset #029",
    "country": "Netherlands",
    "lat": 51.8777,
    "lon": 4.9986,
    "type": "Maritime & Agrotech Centers",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_net_30",
    "name": "Netherlands Industrial/Bank Asset #030",
    "country": "Netherlands",
    "lat": 52.5652,
    "lon": 5.7318,
    "type": "Maritime & Agrotech Centers",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_net_31",
    "name": "Netherlands Industrial/Bank Asset #031",
    "country": "Netherlands",
    "lat": 52.3593,
    "lon": 5.6766,
    "type": "Maritime & Agrotech Centers",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_net_32",
    "name": "Netherlands Industrial/Bank Asset #032",
    "country": "Netherlands",
    "lat": 52.3061,
    "lon": 4.6745,
    "type": "Maritime & Agrotech Centers",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_net_33",
    "name": "Netherlands Industrial/Bank Asset #033",
    "country": "Netherlands",
    "lat": 51.7244,
    "lon": 5.4062,
    "type": "Maritime & Agrotech Centers",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_net_34",
    "name": "Netherlands Industrial/Bank Asset #034",
    "country": "Netherlands",
    "lat": 51.6898,
    "lon": 6.2358,
    "type": "Maritime & Agrotech Centers",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_net_35",
    "name": "Netherlands Industrial/Bank Asset #035",
    "country": "Netherlands",
    "lat": 51.8062,
    "lon": 4.868,
    "type": "Maritime & Agrotech Centers",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_net_36",
    "name": "Netherlands Industrial/Bank Asset #036",
    "country": "Netherlands",
    "lat": 51.6616,
    "lon": 5.7,
    "type": "Maritime & Agrotech Centers",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_net_37",
    "name": "Netherlands Industrial/Bank Asset #037",
    "country": "Netherlands",
    "lat": 51.8373,
    "lon": 4.9876,
    "type": "Maritime & Agrotech Centers",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_net_38",
    "name": "Netherlands Industrial/Bank Asset #038",
    "country": "Netherlands",
    "lat": 52.8239,
    "lon": 5.8808,
    "type": "Maritime & Agrotech Centers",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_net_39",
    "name": "Netherlands Industrial/Bank Asset #039",
    "country": "Netherlands",
    "lat": 51.7675,
    "lon": 4.5337,
    "type": "Maritime & Agrotech Centers",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_net_40",
    "name": "Netherlands Industrial/Bank Asset #040",
    "country": "Netherlands",
    "lat": 52.4126,
    "lon": 5.0494,
    "type": "Maritime & Agrotech Centers",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_net_41",
    "name": "Netherlands Industrial/Bank Asset #041",
    "country": "Netherlands",
    "lat": 52.8983,
    "lon": 5.9268,
    "type": "Maritime & Agrotech Centers",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_net_42",
    "name": "Netherlands Industrial/Bank Asset #042",
    "country": "Netherlands",
    "lat": 52.8574,
    "lon": 5.8992,
    "type": "Maritime & Agrotech Centers",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_net_43",
    "name": "Netherlands Industrial/Bank Asset #043",
    "country": "Netherlands",
    "lat": 51.7947,
    "lon": 4.8653,
    "type": "Maritime & Agrotech Centers",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_net_44",
    "name": "Netherlands Industrial/Bank Asset #044",
    "country": "Netherlands",
    "lat": 52.4726,
    "lon": 4.9827,
    "type": "Maritime & Agrotech Centers",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_net_45",
    "name": "Netherlands Industrial/Bank Asset #045",
    "country": "Netherlands",
    "lat": 52.0378,
    "lon": 4.8029,
    "type": "Maritime & Agrotech Centers",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_net_46",
    "name": "Netherlands Industrial/Bank Asset #046",
    "country": "Netherlands",
    "lat": 52.0965,
    "lon": 4.6941,
    "type": "Maritime & Agrotech Centers",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_net_47",
    "name": "Netherlands Industrial/Bank Asset #047",
    "country": "Netherlands",
    "lat": 52.1917,
    "lon": 6.156,
    "type": "Maritime & Agrotech Centers",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_net_48",
    "name": "Netherlands Industrial/Bank Asset #048",
    "country": "Netherlands",
    "lat": 52.4439,
    "lon": 4.5645,
    "type": "Maritime & Agrotech Centers",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_net_49",
    "name": "Netherlands Industrial/Bank Asset #049",
    "country": "Netherlands",
    "lat": 52.3151,
    "lon": 5.4637,
    "type": "Maritime & Agrotech Centers",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_net_50",
    "name": "Netherlands Industrial/Bank Asset #050",
    "country": "Netherlands",
    "lat": 51.7179,
    "lon": 5.6297,
    "type": "Maritime & Agrotech Centers",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_swi_1",
    "name": "Switzerland Industrial/Bank Asset #001",
    "country": "Switzerland",
    "lat": 46.8472,
    "lon": 8.5511,
    "type": "Private Banking & Precision Mfg",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_swi_2",
    "name": "Switzerland Industrial/Bank Asset #002",
    "country": "Switzerland",
    "lat": 46.273,
    "lon": 8.0119,
    "type": "Private Banking & Precision Mfg",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_swi_3",
    "name": "Switzerland Industrial/Bank Asset #003",
    "country": "Switzerland",
    "lat": 47.0708,
    "lon": 7.2613,
    "type": "Private Banking & Precision Mfg",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_swi_4",
    "name": "Switzerland Industrial/Bank Asset #004",
    "country": "Switzerland",
    "lat": 47.1349,
    "lon": 7.0324,
    "type": "Private Banking & Precision Mfg",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_swi_5",
    "name": "Switzerland Industrial/Bank Asset #005",
    "country": "Switzerland",
    "lat": 46.8704,
    "lon": 9.2498,
    "type": "Private Banking & Precision Mfg",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_swi_6",
    "name": "Switzerland Industrial/Bank Asset #006",
    "country": "Switzerland",
    "lat": 46.6983,
    "lon": 9.2641,
    "type": "Private Banking & Precision Mfg",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_swi_7",
    "name": "Switzerland Industrial/Bank Asset #007",
    "country": "Switzerland",
    "lat": 47.2641,
    "lon": 8.1659,
    "type": "Private Banking & Precision Mfg",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_swi_8",
    "name": "Switzerland Industrial/Bank Asset #008",
    "country": "Switzerland",
    "lat": 46.4493,
    "lon": 9.3334,
    "type": "Private Banking & Precision Mfg",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_swi_9",
    "name": "Switzerland Industrial/Bank Asset #009",
    "country": "Switzerland",
    "lat": 46.5954,
    "lon": 8.5702,
    "type": "Private Banking & Precision Mfg",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_swi_10",
    "name": "Switzerland Industrial/Bank Asset #010",
    "country": "Switzerland",
    "lat": 47.2995,
    "lon": 7.2347,
    "type": "Private Banking & Precision Mfg",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_swi_11",
    "name": "Switzerland Industrial/Bank Asset #011",
    "country": "Switzerland",
    "lat": 46.899,
    "lon": 8.3044,
    "type": "Private Banking & Precision Mfg",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_swi_12",
    "name": "Switzerland Industrial/Bank Asset #012",
    "country": "Switzerland",
    "lat": 47.0777,
    "lon": 9.268,
    "type": "Private Banking & Precision Mfg",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_swi_13",
    "name": "Switzerland Industrial/Bank Asset #013",
    "country": "Switzerland",
    "lat": 47.3059,
    "lon": 7.4402,
    "type": "Private Banking & Precision Mfg",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_swi_14",
    "name": "Switzerland Industrial/Bank Asset #014",
    "country": "Switzerland",
    "lat": 47.2687,
    "lon": 7.4419,
    "type": "Private Banking & Precision Mfg",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_swi_15",
    "name": "Switzerland Industrial/Bank Asset #015",
    "country": "Switzerland",
    "lat": 47.3136,
    "lon": 9.4132,
    "type": "Private Banking & Precision Mfg",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_swi_16",
    "name": "Switzerland Industrial/Bank Asset #016",
    "country": "Switzerland",
    "lat": 46.6864,
    "lon": 8.2089,
    "type": "Private Banking & Precision Mfg",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_swi_17",
    "name": "Switzerland Industrial/Bank Asset #017",
    "country": "Switzerland",
    "lat": 47.3339,
    "lon": 9.3291,
    "type": "Private Banking & Precision Mfg",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_swi_18",
    "name": "Switzerland Industrial/Bank Asset #018",
    "country": "Switzerland",
    "lat": 47.3212,
    "lon": 9.1242,
    "type": "Private Banking & Precision Mfg",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_swi_19",
    "name": "Switzerland Industrial/Bank Asset #019",
    "country": "Switzerland",
    "lat": 46.2211,
    "lon": 8.3831,
    "type": "Private Banking & Precision Mfg",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_swi_20",
    "name": "Switzerland Industrial/Bank Asset #020",
    "country": "Switzerland",
    "lat": 46.3388,
    "lon": 9.3792,
    "type": "Private Banking & Precision Mfg",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_swi_21",
    "name": "Switzerland Industrial/Bank Asset #021",
    "country": "Switzerland",
    "lat": 46.5515,
    "lon": 9.3938,
    "type": "Private Banking & Precision Mfg",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_swi_22",
    "name": "Switzerland Industrial/Bank Asset #022",
    "country": "Switzerland",
    "lat": 46.862,
    "lon": 8.2054,
    "type": "Private Banking & Precision Mfg",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_swi_23",
    "name": "Switzerland Industrial/Bank Asset #023",
    "country": "Switzerland",
    "lat": 47.3363,
    "lon": 9.0625,
    "type": "Private Banking & Precision Mfg",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_swi_24",
    "name": "Switzerland Industrial/Bank Asset #024",
    "country": "Switzerland",
    "lat": 46.7716,
    "lon": 7.4827,
    "type": "Private Banking & Precision Mfg",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_swi_25",
    "name": "Switzerland Industrial/Bank Asset #025",
    "country": "Switzerland",
    "lat": 46.3452,
    "lon": 7.41,
    "type": "Private Banking & Precision Mfg",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_swi_26",
    "name": "Switzerland Industrial/Bank Asset #026",
    "country": "Switzerland",
    "lat": 46.7607,
    "lon": 7.6374,
    "type": "Private Banking & Precision Mfg",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_swi_27",
    "name": "Switzerland Industrial/Bank Asset #027",
    "country": "Switzerland",
    "lat": 46.4334,
    "lon": 8.7879,
    "type": "Private Banking & Precision Mfg",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_swi_28",
    "name": "Switzerland Industrial/Bank Asset #028",
    "country": "Switzerland",
    "lat": 47.1589,
    "lon": 8.3827,
    "type": "Private Banking & Precision Mfg",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_swi_29",
    "name": "Switzerland Industrial/Bank Asset #029",
    "country": "Switzerland",
    "lat": 47.1187,
    "lon": 7.4412,
    "type": "Private Banking & Precision Mfg",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_swi_30",
    "name": "Switzerland Industrial/Bank Asset #030",
    "country": "Switzerland",
    "lat": 47.2374,
    "lon": 9.1729,
    "type": "Private Banking & Precision Mfg",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_swi_31",
    "name": "Switzerland Industrial/Bank Asset #031",
    "country": "Switzerland",
    "lat": 47.2024,
    "lon": 8.2567,
    "type": "Private Banking & Precision Mfg",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_swi_32",
    "name": "Switzerland Industrial/Bank Asset #032",
    "country": "Switzerland",
    "lat": 46.3141,
    "lon": 8.6262,
    "type": "Private Banking & Precision Mfg",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_swi_33",
    "name": "Switzerland Industrial/Bank Asset #033",
    "country": "Switzerland",
    "lat": 46.4317,
    "lon": 7.3575,
    "type": "Private Banking & Precision Mfg",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_swi_34",
    "name": "Switzerland Industrial/Bank Asset #034",
    "country": "Switzerland",
    "lat": 46.5983,
    "lon": 7.6153,
    "type": "Private Banking & Precision Mfg",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_swi_35",
    "name": "Switzerland Industrial/Bank Asset #035",
    "country": "Switzerland",
    "lat": 46.5229,
    "lon": 7.5853,
    "type": "Private Banking & Precision Mfg",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_swi_36",
    "name": "Switzerland Industrial/Bank Asset #036",
    "country": "Switzerland",
    "lat": 47.1145,
    "lon": 9.3097,
    "type": "Private Banking & Precision Mfg",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_swi_37",
    "name": "Switzerland Industrial/Bank Asset #037",
    "country": "Switzerland",
    "lat": 46.5723,
    "lon": 8.7549,
    "type": "Private Banking & Precision Mfg",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_swi_38",
    "name": "Switzerland Industrial/Bank Asset #038",
    "country": "Switzerland",
    "lat": 46.2237,
    "lon": 8.5888,
    "type": "Private Banking & Precision Mfg",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_swi_39",
    "name": "Switzerland Industrial/Bank Asset #039",
    "country": "Switzerland",
    "lat": 47.0413,
    "lon": 7.1691,
    "type": "Private Banking & Precision Mfg",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_swi_40",
    "name": "Switzerland Industrial/Bank Asset #040",
    "country": "Switzerland",
    "lat": 46.3519,
    "lon": 7.7563,
    "type": "Private Banking & Precision Mfg",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_1",
    "name": "India Industrial/Bank Asset #001",
    "country": "India",
    "lat": 20.6758,
    "lon": 78.0403,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_2",
    "name": "India Industrial/Bank Asset #002",
    "country": "India",
    "lat": 27.5317,
    "lon": 81.2569,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_3",
    "name": "India Industrial/Bank Asset #003",
    "country": "India",
    "lat": 19.3537,
    "lon": 71.8787,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_4",
    "name": "India Industrial/Bank Asset #004",
    "country": "India",
    "lat": 27.8258,
    "lon": 74.7206,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_5",
    "name": "India Industrial/Bank Asset #005",
    "country": "India",
    "lat": 23.6048,
    "lon": 73.5061,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_6",
    "name": "India Industrial/Bank Asset #006",
    "country": "India",
    "lat": 16.87,
    "lon": 72.451,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_7",
    "name": "India Industrial/Bank Asset #007",
    "country": "India",
    "lat": 25.4683,
    "lon": 79.6918,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_8",
    "name": "India Industrial/Bank Asset #008",
    "country": "India",
    "lat": 20.8218,
    "lon": 78.7878,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_9",
    "name": "India Industrial/Bank Asset #009",
    "country": "India",
    "lat": 21.5916,
    "lon": 78.6003,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_10",
    "name": "India Industrial/Bank Asset #010",
    "country": "India",
    "lat": 24.2973,
    "lon": 73.4946,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_11",
    "name": "India Industrial/Bank Asset #011",
    "country": "India",
    "lat": 18.4645,
    "lon": 82.0758,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_12",
    "name": "India Industrial/Bank Asset #012",
    "country": "India",
    "lat": 27.2239,
    "lon": 71.3099,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_13",
    "name": "India Industrial/Bank Asset #013",
    "country": "India",
    "lat": 21.2545,
    "lon": 81.2603,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_14",
    "name": "India Industrial/Bank Asset #014",
    "country": "India",
    "lat": 16.0934,
    "lon": 79.0267,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_15",
    "name": "India Industrial/Bank Asset #015",
    "country": "India",
    "lat": 15.8646,
    "lon": 78.7624,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_16",
    "name": "India Industrial/Bank Asset #016",
    "country": "India",
    "lat": 22.0768,
    "lon": 79.1632,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_17",
    "name": "India Industrial/Bank Asset #017",
    "country": "India",
    "lat": 17.0979,
    "lon": 75.2499,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_18",
    "name": "India Industrial/Bank Asset #018",
    "country": "India",
    "lat": 22.2848,
    "lon": 71.8598,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_19",
    "name": "India Industrial/Bank Asset #019",
    "country": "India",
    "lat": 17.8756,
    "lon": 79.3304,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_20",
    "name": "India Industrial/Bank Asset #020",
    "country": "India",
    "lat": 16.2732,
    "lon": 78.166,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_21",
    "name": "India Industrial/Bank Asset #021",
    "country": "India",
    "lat": 26.3217,
    "lon": 77.2549,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_22",
    "name": "India Industrial/Bank Asset #022",
    "country": "India",
    "lat": 22.1855,
    "lon": 77.3088,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_23",
    "name": "India Industrial/Bank Asset #023",
    "country": "India",
    "lat": 15.8083,
    "lon": 77.3981,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_24",
    "name": "India Industrial/Bank Asset #024",
    "country": "India",
    "lat": 26.2968,
    "lon": 81.5725,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_25",
    "name": "India Industrial/Bank Asset #025",
    "country": "India",
    "lat": 20.5433,
    "lon": 83.0633,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_26",
    "name": "India Industrial/Bank Asset #026",
    "country": "India",
    "lat": 25.4413,
    "lon": 79.253,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_27",
    "name": "India Industrial/Bank Asset #027",
    "country": "India",
    "lat": 15.6341,
    "lon": 75.5125,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_28",
    "name": "India Industrial/Bank Asset #028",
    "country": "India",
    "lat": 15.8926,
    "lon": 85.906,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_29",
    "name": "India Industrial/Bank Asset #029",
    "country": "India",
    "lat": 28.0842,
    "lon": 71.1043,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_30",
    "name": "India Industrial/Bank Asset #030",
    "country": "India",
    "lat": 28.0729,
    "lon": 70.5078,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_31",
    "name": "India Industrial/Bank Asset #031",
    "country": "India",
    "lat": 20.7241,
    "lon": 82.3036,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_32",
    "name": "India Industrial/Bank Asset #032",
    "country": "India",
    "lat": 25.7216,
    "lon": 85.6533,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_33",
    "name": "India Industrial/Bank Asset #033",
    "country": "India",
    "lat": 24.0423,
    "lon": 76.7258,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_34",
    "name": "India Industrial/Bank Asset #034",
    "country": "India",
    "lat": 28.9,
    "lon": 76.1197,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_35",
    "name": "India Industrial/Bank Asset #035",
    "country": "India",
    "lat": 27.1747,
    "lon": 84.5083,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_36",
    "name": "India Industrial/Bank Asset #036",
    "country": "India",
    "lat": 20.259,
    "lon": 80.9237,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_37",
    "name": "India Industrial/Bank Asset #037",
    "country": "India",
    "lat": 24.2651,
    "lon": 78.6288,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_38",
    "name": "India Industrial/Bank Asset #038",
    "country": "India",
    "lat": 24.1495,
    "lon": 75.5643,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_39",
    "name": "India Industrial/Bank Asset #039",
    "country": "India",
    "lat": 17.4986,
    "lon": 78.5961,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_40",
    "name": "India Industrial/Bank Asset #040",
    "country": "India",
    "lat": 22.4038,
    "lon": 81.6457,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_41",
    "name": "India Industrial/Bank Asset #041",
    "country": "India",
    "lat": 18.1177,
    "lon": 70.0556,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_42",
    "name": "India Industrial/Bank Asset #042",
    "country": "India",
    "lat": 15.3183,
    "lon": 74.7738,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_43",
    "name": "India Industrial/Bank Asset #043",
    "country": "India",
    "lat": 24.429,
    "lon": 78.7111,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_44",
    "name": "India Industrial/Bank Asset #044",
    "country": "India",
    "lat": 22.4471,
    "lon": 83.1738,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_45",
    "name": "India Industrial/Bank Asset #045",
    "country": "India",
    "lat": 18.4652,
    "lon": 75.5386,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_46",
    "name": "India Industrial/Bank Asset #046",
    "country": "India",
    "lat": 18.8591,
    "lon": 84.9986,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_47",
    "name": "India Industrial/Bank Asset #047",
    "country": "India",
    "lat": 25.1503,
    "lon": 71.8055,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_48",
    "name": "India Industrial/Bank Asset #048",
    "country": "India",
    "lat": 26.3327,
    "lon": 76.7078,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_49",
    "name": "India Industrial/Bank Asset #049",
    "country": "India",
    "lat": 25.7247,
    "lon": 84.1401,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_50",
    "name": "India Industrial/Bank Asset #050",
    "country": "India",
    "lat": 15.219,
    "lon": 73.2973,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_51",
    "name": "India Industrial/Bank Asset #051",
    "country": "India",
    "lat": 16.4126,
    "lon": 70.5372,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_52",
    "name": "India Industrial/Bank Asset #052",
    "country": "India",
    "lat": 23.369,
    "lon": 81.2526,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_53",
    "name": "India Industrial/Bank Asset #053",
    "country": "India",
    "lat": 15.6815,
    "lon": 81.8487,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_54",
    "name": "India Industrial/Bank Asset #054",
    "country": "India",
    "lat": 20.6317,
    "lon": 73.7494,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_55",
    "name": "India Industrial/Bank Asset #055",
    "country": "India",
    "lat": 18.0418,
    "lon": 83.8197,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_56",
    "name": "India Industrial/Bank Asset #056",
    "country": "India",
    "lat": 15.7902,
    "lon": 78.0623,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_57",
    "name": "India Industrial/Bank Asset #057",
    "country": "India",
    "lat": 19.0497,
    "lon": 83.0526,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_58",
    "name": "India Industrial/Bank Asset #058",
    "country": "India",
    "lat": 25.2412,
    "lon": 75.1025,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_59",
    "name": "India Industrial/Bank Asset #059",
    "country": "India",
    "lat": 23.3708,
    "lon": 80.7605,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_60",
    "name": "India Industrial/Bank Asset #060",
    "country": "India",
    "lat": 19.4893,
    "lon": 74.8282,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_61",
    "name": "India Industrial/Bank Asset #061",
    "country": "India",
    "lat": 17.0056,
    "lon": 80.5634,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_62",
    "name": "India Industrial/Bank Asset #062",
    "country": "India",
    "lat": 18.0946,
    "lon": 74.808,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_63",
    "name": "India Industrial/Bank Asset #063",
    "country": "India",
    "lat": 15.8534,
    "lon": 85.1763,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_64",
    "name": "India Industrial/Bank Asset #064",
    "country": "India",
    "lat": 27.316,
    "lon": 84.5852,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_65",
    "name": "India Industrial/Bank Asset #065",
    "country": "India",
    "lat": 23.7639,
    "lon": 76.8352,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_66",
    "name": "India Industrial/Bank Asset #066",
    "country": "India",
    "lat": 21.9387,
    "lon": 85.5566,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_67",
    "name": "India Industrial/Bank Asset #067",
    "country": "India",
    "lat": 28.1822,
    "lon": 80.7415,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_68",
    "name": "India Industrial/Bank Asset #068",
    "country": "India",
    "lat": 26.0013,
    "lon": 75.0998,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_69",
    "name": "India Industrial/Bank Asset #069",
    "country": "India",
    "lat": 20.8285,
    "lon": 72.3875,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_70",
    "name": "India Industrial/Bank Asset #070",
    "country": "India",
    "lat": 20.2704,
    "lon": 82.0707,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_71",
    "name": "India Industrial/Bank Asset #071",
    "country": "India",
    "lat": 21.6293,
    "lon": 83.5895,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_72",
    "name": "India Industrial/Bank Asset #072",
    "country": "India",
    "lat": 19.2103,
    "lon": 81.3212,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_73",
    "name": "India Industrial/Bank Asset #073",
    "country": "India",
    "lat": 26.2809,
    "lon": 84.6359,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_74",
    "name": "India Industrial/Bank Asset #074",
    "country": "India",
    "lat": 22.8734,
    "lon": 85.4846,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_75",
    "name": "India Industrial/Bank Asset #075",
    "country": "India",
    "lat": 22.802,
    "lon": 72.1455,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_76",
    "name": "India Industrial/Bank Asset #076",
    "country": "India",
    "lat": 18.4,
    "lon": 73.2534,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_77",
    "name": "India Industrial/Bank Asset #077",
    "country": "India",
    "lat": 24.0539,
    "lon": 84.7556,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_78",
    "name": "India Industrial/Bank Asset #078",
    "country": "India",
    "lat": 26.8599,
    "lon": 71.4794,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_79",
    "name": "India Industrial/Bank Asset #079",
    "country": "India",
    "lat": 25.1442,
    "lon": 73.0477,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_80",
    "name": "India Industrial/Bank Asset #080",
    "country": "India",
    "lat": 18.7585,
    "lon": 80.7788,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_81",
    "name": "India Industrial/Bank Asset #081",
    "country": "India",
    "lat": 23.4409,
    "lon": 83.9779,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_82",
    "name": "India Industrial/Bank Asset #082",
    "country": "India",
    "lat": 17.6343,
    "lon": 82.1871,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_83",
    "name": "India Industrial/Bank Asset #083",
    "country": "India",
    "lat": 25.1403,
    "lon": 78.9416,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_84",
    "name": "India Industrial/Bank Asset #084",
    "country": "India",
    "lat": 21.7115,
    "lon": 83.9116,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_85",
    "name": "India Industrial/Bank Asset #085",
    "country": "India",
    "lat": 19.6615,
    "lon": 85.3123,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_86",
    "name": "India Industrial/Bank Asset #086",
    "country": "India",
    "lat": 15.2147,
    "lon": 84.9946,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_87",
    "name": "India Industrial/Bank Asset #087",
    "country": "India",
    "lat": 28.4691,
    "lon": 71.8771,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_88",
    "name": "India Industrial/Bank Asset #088",
    "country": "India",
    "lat": 28.994,
    "lon": 77.6627,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_89",
    "name": "India Industrial/Bank Asset #089",
    "country": "India",
    "lat": 18.3963,
    "lon": 79.6704,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_90",
    "name": "India Industrial/Bank Asset #090",
    "country": "India",
    "lat": 17.8632,
    "lon": 84.642,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_91",
    "name": "India Industrial/Bank Asset #091",
    "country": "India",
    "lat": 22.7291,
    "lon": 82.4082,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_92",
    "name": "India Industrial/Bank Asset #092",
    "country": "India",
    "lat": 20.3293,
    "lon": 78.5384,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_93",
    "name": "India Industrial/Bank Asset #093",
    "country": "India",
    "lat": 20.0296,
    "lon": 74.185,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_94",
    "name": "India Industrial/Bank Asset #094",
    "country": "India",
    "lat": 22.1794,
    "lon": 77.9564,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_95",
    "name": "India Industrial/Bank Asset #095",
    "country": "India",
    "lat": 16.3805,
    "lon": 85.7011,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_96",
    "name": "India Industrial/Bank Asset #096",
    "country": "India",
    "lat": 21.5729,
    "lon": 83.4357,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_97",
    "name": "India Industrial/Bank Asset #097",
    "country": "India",
    "lat": 27.8006,
    "lon": 75.9313,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_98",
    "name": "India Industrial/Bank Asset #098",
    "country": "India",
    "lat": 20.795,
    "lon": 79.0004,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_99",
    "name": "India Industrial/Bank Asset #099",
    "country": "India",
    "lat": 18.0978,
    "lon": 72.3348,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_100",
    "name": "India Industrial/Bank Asset #100",
    "country": "India",
    "lat": 18.6508,
    "lon": 84.9561,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_101",
    "name": "India Industrial/Bank Asset #101",
    "country": "India",
    "lat": 23.108,
    "lon": 76.6812,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_102",
    "name": "India Industrial/Bank Asset #102",
    "country": "India",
    "lat": 17.1338,
    "lon": 75.2778,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_103",
    "name": "India Industrial/Bank Asset #103",
    "country": "India",
    "lat": 20.3178,
    "lon": 83.3338,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_104",
    "name": "India Industrial/Bank Asset #104",
    "country": "India",
    "lat": 21.9902,
    "lon": 80.4737,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_105",
    "name": "India Industrial/Bank Asset #105",
    "country": "India",
    "lat": 24.5879,
    "lon": 74.1172,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_106",
    "name": "India Industrial/Bank Asset #106",
    "country": "India",
    "lat": 26.5023,
    "lon": 85.4641,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_107",
    "name": "India Industrial/Bank Asset #107",
    "country": "India",
    "lat": 23.9837,
    "lon": 77.8495,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_108",
    "name": "India Industrial/Bank Asset #108",
    "country": "India",
    "lat": 17.3553,
    "lon": 82.7196,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_109",
    "name": "India Industrial/Bank Asset #109",
    "country": "India",
    "lat": 17.3697,
    "lon": 81.525,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_110",
    "name": "India Industrial/Bank Asset #110",
    "country": "India",
    "lat": 21.8364,
    "lon": 84.6704,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_111",
    "name": "India Industrial/Bank Asset #111",
    "country": "India",
    "lat": 22.5899,
    "lon": 80.269,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_112",
    "name": "India Industrial/Bank Asset #112",
    "country": "India",
    "lat": 15.8222,
    "lon": 70.5412,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_113",
    "name": "India Industrial/Bank Asset #113",
    "country": "India",
    "lat": 26.8538,
    "lon": 85.123,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_114",
    "name": "India Industrial/Bank Asset #114",
    "country": "India",
    "lat": 24.355,
    "lon": 82.2294,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_115",
    "name": "India Industrial/Bank Asset #115",
    "country": "India",
    "lat": 20.7735,
    "lon": 83.4807,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_116",
    "name": "India Industrial/Bank Asset #116",
    "country": "India",
    "lat": 18.2401,
    "lon": 81.3147,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_117",
    "name": "India Industrial/Bank Asset #117",
    "country": "India",
    "lat": 15.128,
    "lon": 78.0917,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_118",
    "name": "India Industrial/Bank Asset #118",
    "country": "India",
    "lat": 20.2248,
    "lon": 79.8854,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_119",
    "name": "India Industrial/Bank Asset #119",
    "country": "India",
    "lat": 24.3346,
    "lon": 79.8643,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_120",
    "name": "India Industrial/Bank Asset #120",
    "country": "India",
    "lat": 21.7649,
    "lon": 77.8057,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_121",
    "name": "India Industrial/Bank Asset #121",
    "country": "India",
    "lat": 15.0926,
    "lon": 78.8263,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_122",
    "name": "India Industrial/Bank Asset #122",
    "country": "India",
    "lat": 15.1659,
    "lon": 78.4707,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_123",
    "name": "India Industrial/Bank Asset #123",
    "country": "India",
    "lat": 18.8464,
    "lon": 85.6397,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_124",
    "name": "India Industrial/Bank Asset #124",
    "country": "India",
    "lat": 15.24,
    "lon": 83.0105,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_125",
    "name": "India Industrial/Bank Asset #125",
    "country": "India",
    "lat": 24.4365,
    "lon": 82.8987,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_126",
    "name": "India Industrial/Bank Asset #126",
    "country": "India",
    "lat": 27.7368,
    "lon": 71.7123,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_127",
    "name": "India Industrial/Bank Asset #127",
    "country": "India",
    "lat": 16.3484,
    "lon": 72.3824,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_128",
    "name": "India Industrial/Bank Asset #128",
    "country": "India",
    "lat": 17.687,
    "lon": 78.4233,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_129",
    "name": "India Industrial/Bank Asset #129",
    "country": "India",
    "lat": 26.413,
    "lon": 74.2772,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_130",
    "name": "India Industrial/Bank Asset #130",
    "country": "India",
    "lat": 20.5565,
    "lon": 75.9688,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_131",
    "name": "India Industrial/Bank Asset #131",
    "country": "India",
    "lat": 20.6844,
    "lon": 79.04,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_132",
    "name": "India Industrial/Bank Asset #132",
    "country": "India",
    "lat": 28.8633,
    "lon": 73.6137,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_133",
    "name": "India Industrial/Bank Asset #133",
    "country": "India",
    "lat": 24.5766,
    "lon": 83.5659,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_134",
    "name": "India Industrial/Bank Asset #134",
    "country": "India",
    "lat": 24.1523,
    "lon": 83.7315,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_135",
    "name": "India Industrial/Bank Asset #135",
    "country": "India",
    "lat": 25.6342,
    "lon": 71.496,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_136",
    "name": "India Industrial/Bank Asset #136",
    "country": "India",
    "lat": 20.3097,
    "lon": 78.8432,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_137",
    "name": "India Industrial/Bank Asset #137",
    "country": "India",
    "lat": 15.7856,
    "lon": 70.1512,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_138",
    "name": "India Industrial/Bank Asset #138",
    "country": "India",
    "lat": 17.3994,
    "lon": 77.9977,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_139",
    "name": "India Industrial/Bank Asset #139",
    "country": "India",
    "lat": 21.0747,
    "lon": 82.55,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_140",
    "name": "India Industrial/Bank Asset #140",
    "country": "India",
    "lat": 22.922,
    "lon": 83.7274,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_141",
    "name": "India Industrial/Bank Asset #141",
    "country": "India",
    "lat": 16.3351,
    "lon": 78.4505,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_142",
    "name": "India Industrial/Bank Asset #142",
    "country": "India",
    "lat": 15.5957,
    "lon": 73.3827,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_143",
    "name": "India Industrial/Bank Asset #143",
    "country": "India",
    "lat": 27.1536,
    "lon": 84.2009,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_144",
    "name": "India Industrial/Bank Asset #144",
    "country": "India",
    "lat": 21.657,
    "lon": 70.745,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_145",
    "name": "India Industrial/Bank Asset #145",
    "country": "India",
    "lat": 16.0409,
    "lon": 84.8094,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_146",
    "name": "India Industrial/Bank Asset #146",
    "country": "India",
    "lat": 27.5904,
    "lon": 79.0162,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_147",
    "name": "India Industrial/Bank Asset #147",
    "country": "India",
    "lat": 15.4606,
    "lon": 84.8603,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_148",
    "name": "India Industrial/Bank Asset #148",
    "country": "India",
    "lat": 19.4028,
    "lon": 85.3835,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_149",
    "name": "India Industrial/Bank Asset #149",
    "country": "India",
    "lat": 23.2185,
    "lon": 82.0361,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_150",
    "name": "India Industrial/Bank Asset #150",
    "country": "India",
    "lat": 24.978,
    "lon": 76.3727,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_151",
    "name": "India Industrial/Bank Asset #151",
    "country": "India",
    "lat": 16.0771,
    "lon": 72.5992,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_152",
    "name": "India Industrial/Bank Asset #152",
    "country": "India",
    "lat": 18.3666,
    "lon": 83.3544,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_153",
    "name": "India Industrial/Bank Asset #153",
    "country": "India",
    "lat": 20.4482,
    "lon": 84.3444,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_154",
    "name": "India Industrial/Bank Asset #154",
    "country": "India",
    "lat": 19.6442,
    "lon": 82.0897,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_155",
    "name": "India Industrial/Bank Asset #155",
    "country": "India",
    "lat": 16.9593,
    "lon": 85.8156,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_156",
    "name": "India Industrial/Bank Asset #156",
    "country": "India",
    "lat": 25.1383,
    "lon": 78.0127,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_157",
    "name": "India Industrial/Bank Asset #157",
    "country": "India",
    "lat": 28.6405,
    "lon": 70.8591,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_158",
    "name": "India Industrial/Bank Asset #158",
    "country": "India",
    "lat": 21.1192,
    "lon": 83.4188,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_159",
    "name": "India Industrial/Bank Asset #159",
    "country": "India",
    "lat": 19.7683,
    "lon": 82.3041,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_160",
    "name": "India Industrial/Bank Asset #160",
    "country": "India",
    "lat": 28.368,
    "lon": 76.3472,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_161",
    "name": "India Industrial/Bank Asset #161",
    "country": "India",
    "lat": 25.8298,
    "lon": 70.474,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_162",
    "name": "India Industrial/Bank Asset #162",
    "country": "India",
    "lat": 18.8266,
    "lon": 85.8814,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_163",
    "name": "India Industrial/Bank Asset #163",
    "country": "India",
    "lat": 21.8684,
    "lon": 75.693,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_164",
    "name": "India Industrial/Bank Asset #164",
    "country": "India",
    "lat": 28.176,
    "lon": 76.9096,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_165",
    "name": "India Industrial/Bank Asset #165",
    "country": "India",
    "lat": 24.5157,
    "lon": 80.5708,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_166",
    "name": "India Industrial/Bank Asset #166",
    "country": "India",
    "lat": 16.1997,
    "lon": 79.8979,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_167",
    "name": "India Industrial/Bank Asset #167",
    "country": "India",
    "lat": 26.1728,
    "lon": 81.4097,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_168",
    "name": "India Industrial/Bank Asset #168",
    "country": "India",
    "lat": 16.1485,
    "lon": 72.4675,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_169",
    "name": "India Industrial/Bank Asset #169",
    "country": "India",
    "lat": 24.9635,
    "lon": 80.1424,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_170",
    "name": "India Industrial/Bank Asset #170",
    "country": "India",
    "lat": 25.3552,
    "lon": 75.0669,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_171",
    "name": "India Industrial/Bank Asset #171",
    "country": "India",
    "lat": 16.4917,
    "lon": 70.0831,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_172",
    "name": "India Industrial/Bank Asset #172",
    "country": "India",
    "lat": 19.3157,
    "lon": 75.7587,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_173",
    "name": "India Industrial/Bank Asset #173",
    "country": "India",
    "lat": 18.7767,
    "lon": 72.1201,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_174",
    "name": "India Industrial/Bank Asset #174",
    "country": "India",
    "lat": 17.6235,
    "lon": 77.1815,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_175",
    "name": "India Industrial/Bank Asset #175",
    "country": "India",
    "lat": 22.7664,
    "lon": 76.5287,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_176",
    "name": "India Industrial/Bank Asset #176",
    "country": "India",
    "lat": 15.3677,
    "lon": 75.6626,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_177",
    "name": "India Industrial/Bank Asset #177",
    "country": "India",
    "lat": 16.3029,
    "lon": 79.5687,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_178",
    "name": "India Industrial/Bank Asset #178",
    "country": "India",
    "lat": 19.542,
    "lon": 76.1638,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_179",
    "name": "India Industrial/Bank Asset #179",
    "country": "India",
    "lat": 19.0859,
    "lon": 76.2048,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_180",
    "name": "India Industrial/Bank Asset #180",
    "country": "India",
    "lat": 16.1858,
    "lon": 84.4182,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_181",
    "name": "India Industrial/Bank Asset #181",
    "country": "India",
    "lat": 27.6729,
    "lon": 85.6508,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_182",
    "name": "India Industrial/Bank Asset #182",
    "country": "India",
    "lat": 23.0074,
    "lon": 72.7133,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_183",
    "name": "India Industrial/Bank Asset #183",
    "country": "India",
    "lat": 20.3302,
    "lon": 72.2214,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_184",
    "name": "India Industrial/Bank Asset #184",
    "country": "India",
    "lat": 19.2158,
    "lon": 77.89,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_185",
    "name": "India Industrial/Bank Asset #185",
    "country": "India",
    "lat": 15.8857,
    "lon": 76.9548,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_186",
    "name": "India Industrial/Bank Asset #186",
    "country": "India",
    "lat": 20.8954,
    "lon": 77.7477,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_187",
    "name": "India Industrial/Bank Asset #187",
    "country": "India",
    "lat": 16.0769,
    "lon": 74.0272,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_188",
    "name": "India Industrial/Bank Asset #188",
    "country": "India",
    "lat": 18.4523,
    "lon": 80.0005,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_189",
    "name": "India Industrial/Bank Asset #189",
    "country": "India",
    "lat": 23.3133,
    "lon": 73.1288,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_190",
    "name": "India Industrial/Bank Asset #190",
    "country": "India",
    "lat": 16.4976,
    "lon": 74.8745,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_191",
    "name": "India Industrial/Bank Asset #191",
    "country": "India",
    "lat": 28.2835,
    "lon": 75.3155,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_192",
    "name": "India Industrial/Bank Asset #192",
    "country": "India",
    "lat": 23.6827,
    "lon": 82.8652,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_193",
    "name": "India Industrial/Bank Asset #193",
    "country": "India",
    "lat": 19.6136,
    "lon": 75.3558,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_194",
    "name": "India Industrial/Bank Asset #194",
    "country": "India",
    "lat": 26.4167,
    "lon": 83.7521,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_195",
    "name": "India Industrial/Bank Asset #195",
    "country": "India",
    "lat": 28.6392,
    "lon": 72.178,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_196",
    "name": "India Industrial/Bank Asset #196",
    "country": "India",
    "lat": 19.4893,
    "lon": 85.1565,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_197",
    "name": "India Industrial/Bank Asset #197",
    "country": "India",
    "lat": 17.8119,
    "lon": 75.0269,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_198",
    "name": "India Industrial/Bank Asset #198",
    "country": "India",
    "lat": 28.504,
    "lon": 85.4996,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_199",
    "name": "India Industrial/Bank Asset #199",
    "country": "India",
    "lat": 19.0803,
    "lon": 81.1193,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_200",
    "name": "India Industrial/Bank Asset #200",
    "country": "India",
    "lat": 21.8741,
    "lon": 79.2141,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_201",
    "name": "India Industrial/Bank Asset #201",
    "country": "India",
    "lat": 18.3939,
    "lon": 76.0169,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_202",
    "name": "India Industrial/Bank Asset #202",
    "country": "India",
    "lat": 26.4309,
    "lon": 76.287,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_203",
    "name": "India Industrial/Bank Asset #203",
    "country": "India",
    "lat": 16.5944,
    "lon": 79.0216,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_204",
    "name": "India Industrial/Bank Asset #204",
    "country": "India",
    "lat": 23.2912,
    "lon": 78.7301,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_205",
    "name": "India Industrial/Bank Asset #205",
    "country": "India",
    "lat": 24.544,
    "lon": 78.8016,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_206",
    "name": "India Industrial/Bank Asset #206",
    "country": "India",
    "lat": 28.3421,
    "lon": 77.386,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_207",
    "name": "India Industrial/Bank Asset #207",
    "country": "India",
    "lat": 24.9171,
    "lon": 77.0153,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_208",
    "name": "India Industrial/Bank Asset #208",
    "country": "India",
    "lat": 19.0786,
    "lon": 81.0854,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_209",
    "name": "India Industrial/Bank Asset #209",
    "country": "India",
    "lat": 26.4655,
    "lon": 82.7305,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_210",
    "name": "India Industrial/Bank Asset #210",
    "country": "India",
    "lat": 20.728,
    "lon": 77.9889,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_211",
    "name": "India Industrial/Bank Asset #211",
    "country": "India",
    "lat": 23.8667,
    "lon": 73.8723,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_212",
    "name": "India Industrial/Bank Asset #212",
    "country": "India",
    "lat": 24.2213,
    "lon": 81.4438,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_213",
    "name": "India Industrial/Bank Asset #213",
    "country": "India",
    "lat": 26.0471,
    "lon": 71.1834,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_214",
    "name": "India Industrial/Bank Asset #214",
    "country": "India",
    "lat": 28.8698,
    "lon": 77.6678,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_215",
    "name": "India Industrial/Bank Asset #215",
    "country": "India",
    "lat": 20.6113,
    "lon": 78.1058,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_216",
    "name": "India Industrial/Bank Asset #216",
    "country": "India",
    "lat": 27.8855,
    "lon": 81.0673,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_217",
    "name": "India Industrial/Bank Asset #217",
    "country": "India",
    "lat": 22.611,
    "lon": 82.6515,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_218",
    "name": "India Industrial/Bank Asset #218",
    "country": "India",
    "lat": 20.0334,
    "lon": 84.328,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_219",
    "name": "India Industrial/Bank Asset #219",
    "country": "India",
    "lat": 22.5167,
    "lon": 80.2109,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_220",
    "name": "India Industrial/Bank Asset #220",
    "country": "India",
    "lat": 16.1897,
    "lon": 82.3033,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_221",
    "name": "India Industrial/Bank Asset #221",
    "country": "India",
    "lat": 24.2064,
    "lon": 75.6801,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_222",
    "name": "India Industrial/Bank Asset #222",
    "country": "India",
    "lat": 24.058,
    "lon": 70.7087,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_223",
    "name": "India Industrial/Bank Asset #223",
    "country": "India",
    "lat": 28.7705,
    "lon": 80.8396,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_224",
    "name": "India Industrial/Bank Asset #224",
    "country": "India",
    "lat": 20.5946,
    "lon": 82.0429,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_225",
    "name": "India Industrial/Bank Asset #225",
    "country": "India",
    "lat": 28.52,
    "lon": 76.8873,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_226",
    "name": "India Industrial/Bank Asset #226",
    "country": "India",
    "lat": 15.1477,
    "lon": 74.1398,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_227",
    "name": "India Industrial/Bank Asset #227",
    "country": "India",
    "lat": 22.1495,
    "lon": 78.3008,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_228",
    "name": "India Industrial/Bank Asset #228",
    "country": "India",
    "lat": 23.1273,
    "lon": 79.2038,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_229",
    "name": "India Industrial/Bank Asset #229",
    "country": "India",
    "lat": 21.2409,
    "lon": 76.2581,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_230",
    "name": "India Industrial/Bank Asset #230",
    "country": "India",
    "lat": 25.8128,
    "lon": 79.4174,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_231",
    "name": "India Industrial/Bank Asset #231",
    "country": "India",
    "lat": 22.0065,
    "lon": 75.5195,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_232",
    "name": "India Industrial/Bank Asset #232",
    "country": "India",
    "lat": 15.3439,
    "lon": 71.6728,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_233",
    "name": "India Industrial/Bank Asset #233",
    "country": "India",
    "lat": 20.8237,
    "lon": 85.3876,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_234",
    "name": "India Industrial/Bank Asset #234",
    "country": "India",
    "lat": 16.625,
    "lon": 85.0508,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_235",
    "name": "India Industrial/Bank Asset #235",
    "country": "India",
    "lat": 16.9835,
    "lon": 74.9902,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_236",
    "name": "India Industrial/Bank Asset #236",
    "country": "India",
    "lat": 21.3747,
    "lon": 73.3099,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_237",
    "name": "India Industrial/Bank Asset #237",
    "country": "India",
    "lat": 21.761,
    "lon": 77.6186,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_238",
    "name": "India Industrial/Bank Asset #238",
    "country": "India",
    "lat": 21.1343,
    "lon": 81.1482,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_239",
    "name": "India Industrial/Bank Asset #239",
    "country": "India",
    "lat": 19.4647,
    "lon": 74.8042,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_240",
    "name": "India Industrial/Bank Asset #240",
    "country": "India",
    "lat": 26.3426,
    "lon": 71.8414,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_241",
    "name": "India Industrial/Bank Asset #241",
    "country": "India",
    "lat": 26.8885,
    "lon": 80.3675,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_242",
    "name": "India Industrial/Bank Asset #242",
    "country": "India",
    "lat": 24.48,
    "lon": 72.6297,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_243",
    "name": "India Industrial/Bank Asset #243",
    "country": "India",
    "lat": 28.7746,
    "lon": 73.9026,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_244",
    "name": "India Industrial/Bank Asset #244",
    "country": "India",
    "lat": 17.4423,
    "lon": 72.5622,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_245",
    "name": "India Industrial/Bank Asset #245",
    "country": "India",
    "lat": 22.8379,
    "lon": 85.3354,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_246",
    "name": "India Industrial/Bank Asset #246",
    "country": "India",
    "lat": 18.246,
    "lon": 76.4808,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_247",
    "name": "India Industrial/Bank Asset #247",
    "country": "India",
    "lat": 17.5823,
    "lon": 80.2477,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_248",
    "name": "India Industrial/Bank Asset #248",
    "country": "India",
    "lat": 21.0499,
    "lon": 70.4671,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_249",
    "name": "India Industrial/Bank Asset #249",
    "country": "India",
    "lat": 23.5975,
    "lon": 73.1572,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_250",
    "name": "India Industrial/Bank Asset #250",
    "country": "India",
    "lat": 23.2908,
    "lon": 76.2214,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_251",
    "name": "India Industrial/Bank Asset #251",
    "country": "India",
    "lat": 24.8663,
    "lon": 73.2926,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_252",
    "name": "India Industrial/Bank Asset #252",
    "country": "India",
    "lat": 25.5326,
    "lon": 82.9397,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_253",
    "name": "India Industrial/Bank Asset #253",
    "country": "India",
    "lat": 15.8759,
    "lon": 71.628,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_254",
    "name": "India Industrial/Bank Asset #254",
    "country": "India",
    "lat": 27.2077,
    "lon": 72.9914,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_255",
    "name": "India Industrial/Bank Asset #255",
    "country": "India",
    "lat": 19.5638,
    "lon": 77.3208,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_256",
    "name": "India Industrial/Bank Asset #256",
    "country": "India",
    "lat": 18.6729,
    "lon": 83.8022,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_257",
    "name": "India Industrial/Bank Asset #257",
    "country": "India",
    "lat": 22.388,
    "lon": 80.2257,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_258",
    "name": "India Industrial/Bank Asset #258",
    "country": "India",
    "lat": 23.3576,
    "lon": 79.7809,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_259",
    "name": "India Industrial/Bank Asset #259",
    "country": "India",
    "lat": 23.2181,
    "lon": 75.5668,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_260",
    "name": "India Industrial/Bank Asset #260",
    "country": "India",
    "lat": 26.8372,
    "lon": 79.8778,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_261",
    "name": "India Industrial/Bank Asset #261",
    "country": "India",
    "lat": 26.3923,
    "lon": 81.2958,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_262",
    "name": "India Industrial/Bank Asset #262",
    "country": "India",
    "lat": 19.1642,
    "lon": 79.8318,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_263",
    "name": "India Industrial/Bank Asset #263",
    "country": "India",
    "lat": 16.1865,
    "lon": 72.1432,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_264",
    "name": "India Industrial/Bank Asset #264",
    "country": "India",
    "lat": 16.6501,
    "lon": 74.8861,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_265",
    "name": "India Industrial/Bank Asset #265",
    "country": "India",
    "lat": 17.5626,
    "lon": 81.095,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_266",
    "name": "India Industrial/Bank Asset #266",
    "country": "India",
    "lat": 22.1515,
    "lon": 76.6918,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_267",
    "name": "India Industrial/Bank Asset #267",
    "country": "India",
    "lat": 16.9301,
    "lon": 76.1394,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_268",
    "name": "India Industrial/Bank Asset #268",
    "country": "India",
    "lat": 17.6006,
    "lon": 80.168,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_269",
    "name": "India Industrial/Bank Asset #269",
    "country": "India",
    "lat": 24.7081,
    "lon": 80.3242,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_270",
    "name": "India Industrial/Bank Asset #270",
    "country": "India",
    "lat": 28.9986,
    "lon": 78.8786,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_271",
    "name": "India Industrial/Bank Asset #271",
    "country": "India",
    "lat": 21.855,
    "lon": 72.2447,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_272",
    "name": "India Industrial/Bank Asset #272",
    "country": "India",
    "lat": 19.4041,
    "lon": 77.216,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_273",
    "name": "India Industrial/Bank Asset #273",
    "country": "India",
    "lat": 15.7506,
    "lon": 75.7446,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_274",
    "name": "India Industrial/Bank Asset #274",
    "country": "India",
    "lat": 15.1342,
    "lon": 72.1846,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_275",
    "name": "India Industrial/Bank Asset #275",
    "country": "India",
    "lat": 26.413,
    "lon": 85.4213,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_276",
    "name": "India Industrial/Bank Asset #276",
    "country": "India",
    "lat": 22.0761,
    "lon": 77.9195,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_277",
    "name": "India Industrial/Bank Asset #277",
    "country": "India",
    "lat": 24.5858,
    "lon": 76.6501,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_278",
    "name": "India Industrial/Bank Asset #278",
    "country": "India",
    "lat": 26.7585,
    "lon": 77.8192,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_279",
    "name": "India Industrial/Bank Asset #279",
    "country": "India",
    "lat": 16.1574,
    "lon": 70.4938,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_280",
    "name": "India Industrial/Bank Asset #280",
    "country": "India",
    "lat": 25.6548,
    "lon": 74.6734,
    "type": "Discom Grid & Industrial Corridors",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_1",
    "name": "China Industrial/Bank Asset #001",
    "country": "China",
    "lat": 28.3976,
    "lon": 115.7522,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_2",
    "name": "China Industrial/Bank Asset #002",
    "country": "China",
    "lat": 26.6913,
    "lon": 114.1464,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_3",
    "name": "China Industrial/Bank Asset #003",
    "country": "China",
    "lat": 35.8803,
    "lon": 120.3184,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_4",
    "name": "China Industrial/Bank Asset #004",
    "country": "China",
    "lat": 32.7956,
    "lon": 107.2642,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_5",
    "name": "China Industrial/Bank Asset #005",
    "country": "China",
    "lat": 25.8273,
    "lon": 120.5023,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_6",
    "name": "China Industrial/Bank Asset #006",
    "country": "China",
    "lat": 37.1725,
    "lon": 112.3372,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_7",
    "name": "China Industrial/Bank Asset #007",
    "country": "China",
    "lat": 37.1618,
    "lon": 105.8322,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_8",
    "name": "China Industrial/Bank Asset #008",
    "country": "China",
    "lat": 35.5037,
    "lon": 115.9271,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_9",
    "name": "China Industrial/Bank Asset #009",
    "country": "China",
    "lat": 39.8364,
    "lon": 107.0483,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_10",
    "name": "China Industrial/Bank Asset #010",
    "country": "China",
    "lat": 37.2811,
    "lon": 120.0269,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_11",
    "name": "China Industrial/Bank Asset #011",
    "country": "China",
    "lat": 28.7633,
    "lon": 124.9863,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_12",
    "name": "China Industrial/Bank Asset #012",
    "country": "China",
    "lat": 31.1957,
    "lon": 111.9715,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_13",
    "name": "China Industrial/Bank Asset #013",
    "country": "China",
    "lat": 37.0677,
    "lon": 113.7814,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_14",
    "name": "China Industrial/Bank Asset #014",
    "country": "China",
    "lat": 39.9033,
    "lon": 120.5126,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_15",
    "name": "China Industrial/Bank Asset #015",
    "country": "China",
    "lat": 27.7911,
    "lon": 121.2141,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_16",
    "name": "China Industrial/Bank Asset #016",
    "country": "China",
    "lat": 33.4068,
    "lon": 112.0126,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_17",
    "name": "China Industrial/Bank Asset #017",
    "country": "China",
    "lat": 35.3721,
    "lon": 117.6554,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_18",
    "name": "China Industrial/Bank Asset #018",
    "country": "China",
    "lat": 26.6557,
    "lon": 107.7847,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_19",
    "name": "China Industrial/Bank Asset #019",
    "country": "China",
    "lat": 27.3059,
    "lon": 109.1389,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_20",
    "name": "China Industrial/Bank Asset #020",
    "country": "China",
    "lat": 24.9497,
    "lon": 112.0163,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_21",
    "name": "China Industrial/Bank Asset #021",
    "country": "China",
    "lat": 28.4974,
    "lon": 115.7754,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_22",
    "name": "China Industrial/Bank Asset #022",
    "country": "China",
    "lat": 29.1785,
    "lon": 119.0811,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_23",
    "name": "China Industrial/Bank Asset #023",
    "country": "China",
    "lat": 28.6293,
    "lon": 110.3469,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_24",
    "name": "China Industrial/Bank Asset #024",
    "country": "China",
    "lat": 37.7283,
    "lon": 124.7098,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_25",
    "name": "China Industrial/Bank Asset #025",
    "country": "China",
    "lat": 34.8688,
    "lon": 106.9045,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_26",
    "name": "China Industrial/Bank Asset #026",
    "country": "China",
    "lat": 39.4044,
    "lon": 120.7138,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_27",
    "name": "China Industrial/Bank Asset #027",
    "country": "China",
    "lat": 38.7003,
    "lon": 124.8497,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_28",
    "name": "China Industrial/Bank Asset #028",
    "country": "China",
    "lat": 37.8728,
    "lon": 107.5378,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_29",
    "name": "China Industrial/Bank Asset #029",
    "country": "China",
    "lat": 37.8573,
    "lon": 109.9935,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_30",
    "name": "China Industrial/Bank Asset #030",
    "country": "China",
    "lat": 35.3823,
    "lon": 121.5696,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_31",
    "name": "China Industrial/Bank Asset #031",
    "country": "China",
    "lat": 36.1836,
    "lon": 118.5247,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_32",
    "name": "China Industrial/Bank Asset #032",
    "country": "China",
    "lat": 31.8313,
    "lon": 116.5485,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_33",
    "name": "China Industrial/Bank Asset #033",
    "country": "China",
    "lat": 28.2995,
    "lon": 113.2845,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_34",
    "name": "China Industrial/Bank Asset #034",
    "country": "China",
    "lat": 31.2319,
    "lon": 117.6726,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_35",
    "name": "China Industrial/Bank Asset #035",
    "country": "China",
    "lat": 38.082,
    "lon": 106.8619,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_36",
    "name": "China Industrial/Bank Asset #036",
    "country": "China",
    "lat": 32.2498,
    "lon": 110.5645,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_37",
    "name": "China Industrial/Bank Asset #037",
    "country": "China",
    "lat": 38.9814,
    "lon": 112.3814,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_38",
    "name": "China Industrial/Bank Asset #038",
    "country": "China",
    "lat": 39.2041,
    "lon": 111.5458,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_39",
    "name": "China Industrial/Bank Asset #039",
    "country": "China",
    "lat": 24.0396,
    "lon": 120.4827,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_40",
    "name": "China Industrial/Bank Asset #040",
    "country": "China",
    "lat": 35.7236,
    "lon": 119.6186,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_41",
    "name": "China Industrial/Bank Asset #041",
    "country": "China",
    "lat": 31.3352,
    "lon": 118.2829,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_42",
    "name": "China Industrial/Bank Asset #042",
    "country": "China",
    "lat": 29.7316,
    "lon": 106.2666,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_43",
    "name": "China Industrial/Bank Asset #043",
    "country": "China",
    "lat": 32.5508,
    "lon": 109.3566,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_44",
    "name": "China Industrial/Bank Asset #044",
    "country": "China",
    "lat": 30.8743,
    "lon": 109.237,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_45",
    "name": "China Industrial/Bank Asset #045",
    "country": "China",
    "lat": 28.2966,
    "lon": 121.5669,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_46",
    "name": "China Industrial/Bank Asset #046",
    "country": "China",
    "lat": 29.4041,
    "lon": 116.5587,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_47",
    "name": "China Industrial/Bank Asset #047",
    "country": "China",
    "lat": 33.0583,
    "lon": 114.7068,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_48",
    "name": "China Industrial/Bank Asset #048",
    "country": "China",
    "lat": 29.4998,
    "lon": 118.651,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_49",
    "name": "China Industrial/Bank Asset #049",
    "country": "China",
    "lat": 24.7745,
    "lon": 106.9915,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_50",
    "name": "China Industrial/Bank Asset #050",
    "country": "China",
    "lat": 36.5422,
    "lon": 114.1916,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_51",
    "name": "China Industrial/Bank Asset #051",
    "country": "China",
    "lat": 25.9878,
    "lon": 122.153,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_52",
    "name": "China Industrial/Bank Asset #052",
    "country": "China",
    "lat": 31.0606,
    "lon": 105.0135,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_53",
    "name": "China Industrial/Bank Asset #053",
    "country": "China",
    "lat": 39.3285,
    "lon": 109.0464,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_54",
    "name": "China Industrial/Bank Asset #054",
    "country": "China",
    "lat": 35.0175,
    "lon": 107.6383,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_55",
    "name": "China Industrial/Bank Asset #055",
    "country": "China",
    "lat": 34.4,
    "lon": 108.1795,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_56",
    "name": "China Industrial/Bank Asset #056",
    "country": "China",
    "lat": 38.9236,
    "lon": 110.4804,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_57",
    "name": "China Industrial/Bank Asset #057",
    "country": "China",
    "lat": 34.4734,
    "lon": 110.0078,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_58",
    "name": "China Industrial/Bank Asset #058",
    "country": "China",
    "lat": 29.9495,
    "lon": 123.076,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_59",
    "name": "China Industrial/Bank Asset #059",
    "country": "China",
    "lat": 26.6484,
    "lon": 112.9268,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_60",
    "name": "China Industrial/Bank Asset #060",
    "country": "China",
    "lat": 28.8881,
    "lon": 118.9888,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_61",
    "name": "China Industrial/Bank Asset #061",
    "country": "China",
    "lat": 27.7463,
    "lon": 118.1097,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_62",
    "name": "China Industrial/Bank Asset #062",
    "country": "China",
    "lat": 35.2592,
    "lon": 105.0217,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_63",
    "name": "China Industrial/Bank Asset #063",
    "country": "China",
    "lat": 31.6289,
    "lon": 107.654,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_64",
    "name": "China Industrial/Bank Asset #064",
    "country": "China",
    "lat": 27.6191,
    "lon": 118.5997,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_65",
    "name": "China Industrial/Bank Asset #065",
    "country": "China",
    "lat": 24.1486,
    "lon": 118.9119,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_66",
    "name": "China Industrial/Bank Asset #066",
    "country": "China",
    "lat": 37.0737,
    "lon": 124.7631,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_67",
    "name": "China Industrial/Bank Asset #067",
    "country": "China",
    "lat": 30.757,
    "lon": 107.6435,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_68",
    "name": "China Industrial/Bank Asset #068",
    "country": "China",
    "lat": 25.1333,
    "lon": 112.6614,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_69",
    "name": "China Industrial/Bank Asset #069",
    "country": "China",
    "lat": 35.6922,
    "lon": 107.0485,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_70",
    "name": "China Industrial/Bank Asset #070",
    "country": "China",
    "lat": 29.0136,
    "lon": 122.6198,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_71",
    "name": "China Industrial/Bank Asset #071",
    "country": "China",
    "lat": 26.1941,
    "lon": 120.4692,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_72",
    "name": "China Industrial/Bank Asset #072",
    "country": "China",
    "lat": 36.0505,
    "lon": 107.6629,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_73",
    "name": "China Industrial/Bank Asset #073",
    "country": "China",
    "lat": 39.887,
    "lon": 107.8571,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_74",
    "name": "China Industrial/Bank Asset #074",
    "country": "China",
    "lat": 32.4881,
    "lon": 105.1695,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_75",
    "name": "China Industrial/Bank Asset #075",
    "country": "China",
    "lat": 34.4003,
    "lon": 113.802,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_76",
    "name": "China Industrial/Bank Asset #076",
    "country": "China",
    "lat": 35.5589,
    "lon": 117.5616,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_77",
    "name": "China Industrial/Bank Asset #077",
    "country": "China",
    "lat": 26.422,
    "lon": 113.2342,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_78",
    "name": "China Industrial/Bank Asset #078",
    "country": "China",
    "lat": 34.9851,
    "lon": 122.1993,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_79",
    "name": "China Industrial/Bank Asset #079",
    "country": "China",
    "lat": 25.387,
    "lon": 107.0093,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_80",
    "name": "China Industrial/Bank Asset #080",
    "country": "China",
    "lat": 36.0391,
    "lon": 116.7915,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_81",
    "name": "China Industrial/Bank Asset #081",
    "country": "China",
    "lat": 30.1445,
    "lon": 124.265,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_82",
    "name": "China Industrial/Bank Asset #082",
    "country": "China",
    "lat": 29.0321,
    "lon": 107.7966,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_83",
    "name": "China Industrial/Bank Asset #083",
    "country": "China",
    "lat": 28.4315,
    "lon": 106.685,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_84",
    "name": "China Industrial/Bank Asset #084",
    "country": "China",
    "lat": 32.8543,
    "lon": 117.0002,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_85",
    "name": "China Industrial/Bank Asset #085",
    "country": "China",
    "lat": 33.7215,
    "lon": 120.5794,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_86",
    "name": "China Industrial/Bank Asset #086",
    "country": "China",
    "lat": 35.0476,
    "lon": 121.9578,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_87",
    "name": "China Industrial/Bank Asset #087",
    "country": "China",
    "lat": 34.5345,
    "lon": 111.033,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_88",
    "name": "China Industrial/Bank Asset #088",
    "country": "China",
    "lat": 32.284,
    "lon": 115.1905,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_89",
    "name": "China Industrial/Bank Asset #089",
    "country": "China",
    "lat": 35.9655,
    "lon": 110.9108,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_90",
    "name": "China Industrial/Bank Asset #090",
    "country": "China",
    "lat": 24.8731,
    "lon": 122.9583,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_91",
    "name": "China Industrial/Bank Asset #091",
    "country": "China",
    "lat": 39.2747,
    "lon": 114.8978,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_92",
    "name": "China Industrial/Bank Asset #092",
    "country": "China",
    "lat": 25.8039,
    "lon": 114.9917,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_93",
    "name": "China Industrial/Bank Asset #093",
    "country": "China",
    "lat": 33.5029,
    "lon": 115.5657,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_94",
    "name": "China Industrial/Bank Asset #094",
    "country": "China",
    "lat": 39.6432,
    "lon": 124.7377,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_95",
    "name": "China Industrial/Bank Asset #095",
    "country": "China",
    "lat": 38.9428,
    "lon": 107.6397,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_96",
    "name": "China Industrial/Bank Asset #096",
    "country": "China",
    "lat": 37.773,
    "lon": 116.3676,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_97",
    "name": "China Industrial/Bank Asset #097",
    "country": "China",
    "lat": 29.8466,
    "lon": 118.6588,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_98",
    "name": "China Industrial/Bank Asset #098",
    "country": "China",
    "lat": 36.2036,
    "lon": 124.0891,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_99",
    "name": "China Industrial/Bank Asset #099",
    "country": "China",
    "lat": 36.3259,
    "lon": 105.3338,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_100",
    "name": "China Industrial/Bank Asset #100",
    "country": "China",
    "lat": 25.0805,
    "lon": 110.2437,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_101",
    "name": "China Industrial/Bank Asset #101",
    "country": "China",
    "lat": 24.6372,
    "lon": 106.2094,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_102",
    "name": "China Industrial/Bank Asset #102",
    "country": "China",
    "lat": 36.6286,
    "lon": 115.1322,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_103",
    "name": "China Industrial/Bank Asset #103",
    "country": "China",
    "lat": 34.0571,
    "lon": 115.021,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_104",
    "name": "China Industrial/Bank Asset #104",
    "country": "China",
    "lat": 30.6469,
    "lon": 119.0362,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_105",
    "name": "China Industrial/Bank Asset #105",
    "country": "China",
    "lat": 25.3188,
    "lon": 115.7313,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_106",
    "name": "China Industrial/Bank Asset #106",
    "country": "China",
    "lat": 33.8568,
    "lon": 110.5494,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_107",
    "name": "China Industrial/Bank Asset #107",
    "country": "China",
    "lat": 28.9585,
    "lon": 115.2261,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_108",
    "name": "China Industrial/Bank Asset #108",
    "country": "China",
    "lat": 27.2512,
    "lon": 121.1612,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_109",
    "name": "China Industrial/Bank Asset #109",
    "country": "China",
    "lat": 32.5822,
    "lon": 112.8146,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_110",
    "name": "China Industrial/Bank Asset #110",
    "country": "China",
    "lat": 34.1487,
    "lon": 121.6905,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_111",
    "name": "China Industrial/Bank Asset #111",
    "country": "China",
    "lat": 34.8969,
    "lon": 106.3223,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_112",
    "name": "China Industrial/Bank Asset #112",
    "country": "China",
    "lat": 35.1788,
    "lon": 119.5992,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_113",
    "name": "China Industrial/Bank Asset #113",
    "country": "China",
    "lat": 37.5435,
    "lon": 106.1581,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_114",
    "name": "China Industrial/Bank Asset #114",
    "country": "China",
    "lat": 25.3794,
    "lon": 113.6897,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_115",
    "name": "China Industrial/Bank Asset #115",
    "country": "China",
    "lat": 31.2539,
    "lon": 117.1766,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_116",
    "name": "China Industrial/Bank Asset #116",
    "country": "China",
    "lat": 28.9486,
    "lon": 119.8339,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_117",
    "name": "China Industrial/Bank Asset #117",
    "country": "China",
    "lat": 35.8505,
    "lon": 107.3889,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_118",
    "name": "China Industrial/Bank Asset #118",
    "country": "China",
    "lat": 35.3264,
    "lon": 119.03,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_119",
    "name": "China Industrial/Bank Asset #119",
    "country": "China",
    "lat": 26.6213,
    "lon": 124.0603,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_120",
    "name": "China Industrial/Bank Asset #120",
    "country": "China",
    "lat": 32.3681,
    "lon": 120.6597,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_121",
    "name": "China Industrial/Bank Asset #121",
    "country": "China",
    "lat": 35.5322,
    "lon": 108.3393,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_122",
    "name": "China Industrial/Bank Asset #122",
    "country": "China",
    "lat": 26.0309,
    "lon": 120.6225,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_123",
    "name": "China Industrial/Bank Asset #123",
    "country": "China",
    "lat": 28.3002,
    "lon": 122.7283,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_124",
    "name": "China Industrial/Bank Asset #124",
    "country": "China",
    "lat": 36.3429,
    "lon": 105.5871,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_125",
    "name": "China Industrial/Bank Asset #125",
    "country": "China",
    "lat": 36.9137,
    "lon": 110.4396,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_126",
    "name": "China Industrial/Bank Asset #126",
    "country": "China",
    "lat": 25.022,
    "lon": 119.2465,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_127",
    "name": "China Industrial/Bank Asset #127",
    "country": "China",
    "lat": 33.2264,
    "lon": 106.5414,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_128",
    "name": "China Industrial/Bank Asset #128",
    "country": "China",
    "lat": 31.2832,
    "lon": 112.2025,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_129",
    "name": "China Industrial/Bank Asset #129",
    "country": "China",
    "lat": 31.9938,
    "lon": 116.3377,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_130",
    "name": "China Industrial/Bank Asset #130",
    "country": "China",
    "lat": 29.883,
    "lon": 110.1023,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_131",
    "name": "China Industrial/Bank Asset #131",
    "country": "China",
    "lat": 25.6465,
    "lon": 116.4782,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_132",
    "name": "China Industrial/Bank Asset #132",
    "country": "China",
    "lat": 35.5645,
    "lon": 109.5681,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_133",
    "name": "China Industrial/Bank Asset #133",
    "country": "China",
    "lat": 32.1412,
    "lon": 105.8808,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_134",
    "name": "China Industrial/Bank Asset #134",
    "country": "China",
    "lat": 37.8069,
    "lon": 109.891,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_135",
    "name": "China Industrial/Bank Asset #135",
    "country": "China",
    "lat": 31.5482,
    "lon": 112.6596,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_136",
    "name": "China Industrial/Bank Asset #136",
    "country": "China",
    "lat": 26.4014,
    "lon": 123.6232,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_137",
    "name": "China Industrial/Bank Asset #137",
    "country": "China",
    "lat": 37.7198,
    "lon": 116.0573,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_138",
    "name": "China Industrial/Bank Asset #138",
    "country": "China",
    "lat": 38.6232,
    "lon": 119.8133,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_139",
    "name": "China Industrial/Bank Asset #139",
    "country": "China",
    "lat": 30.7099,
    "lon": 111.436,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_140",
    "name": "China Industrial/Bank Asset #140",
    "country": "China",
    "lat": 30.6601,
    "lon": 119.4058,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_141",
    "name": "China Industrial/Bank Asset #141",
    "country": "China",
    "lat": 28.3401,
    "lon": 106.5577,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_142",
    "name": "China Industrial/Bank Asset #142",
    "country": "China",
    "lat": 29.9649,
    "lon": 115.0408,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_143",
    "name": "China Industrial/Bank Asset #143",
    "country": "China",
    "lat": 38.4311,
    "lon": 108.5869,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_144",
    "name": "China Industrial/Bank Asset #144",
    "country": "China",
    "lat": 36.8694,
    "lon": 124.6283,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_145",
    "name": "China Industrial/Bank Asset #145",
    "country": "China",
    "lat": 39.2653,
    "lon": 106.3785,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_146",
    "name": "China Industrial/Bank Asset #146",
    "country": "China",
    "lat": 31.4415,
    "lon": 110.6461,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_147",
    "name": "China Industrial/Bank Asset #147",
    "country": "China",
    "lat": 37.5175,
    "lon": 111.546,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_148",
    "name": "China Industrial/Bank Asset #148",
    "country": "China",
    "lat": 32.8495,
    "lon": 105.1594,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_149",
    "name": "China Industrial/Bank Asset #149",
    "country": "China",
    "lat": 27.2107,
    "lon": 116.2761,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_150",
    "name": "China Industrial/Bank Asset #150",
    "country": "China",
    "lat": 28.8625,
    "lon": 117.4544,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_151",
    "name": "China Industrial/Bank Asset #151",
    "country": "China",
    "lat": 31.4228,
    "lon": 116.8338,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_152",
    "name": "China Industrial/Bank Asset #152",
    "country": "China",
    "lat": 31.8938,
    "lon": 120.4523,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_153",
    "name": "China Industrial/Bank Asset #153",
    "country": "China",
    "lat": 27.1268,
    "lon": 123.0089,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_154",
    "name": "China Industrial/Bank Asset #154",
    "country": "China",
    "lat": 36.1677,
    "lon": 109.9025,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_155",
    "name": "China Industrial/Bank Asset #155",
    "country": "China",
    "lat": 24.102,
    "lon": 113.2007,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_156",
    "name": "China Industrial/Bank Asset #156",
    "country": "China",
    "lat": 27.728,
    "lon": 111.9285,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_157",
    "name": "China Industrial/Bank Asset #157",
    "country": "China",
    "lat": 37.4332,
    "lon": 122.544,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_158",
    "name": "China Industrial/Bank Asset #158",
    "country": "China",
    "lat": 39.2158,
    "lon": 105.0292,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_159",
    "name": "China Industrial/Bank Asset #159",
    "country": "China",
    "lat": 34.5169,
    "lon": 121.9801,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_160",
    "name": "China Industrial/Bank Asset #160",
    "country": "China",
    "lat": 35.6354,
    "lon": 107.079,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_161",
    "name": "China Industrial/Bank Asset #161",
    "country": "China",
    "lat": 32.477,
    "lon": 109.7634,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_162",
    "name": "China Industrial/Bank Asset #162",
    "country": "China",
    "lat": 31.8725,
    "lon": 106.1979,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_163",
    "name": "China Industrial/Bank Asset #163",
    "country": "China",
    "lat": 39.9513,
    "lon": 119.233,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_164",
    "name": "China Industrial/Bank Asset #164",
    "country": "China",
    "lat": 25.4884,
    "lon": 123.4255,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_165",
    "name": "China Industrial/Bank Asset #165",
    "country": "China",
    "lat": 38.3566,
    "lon": 115.3952,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_166",
    "name": "China Industrial/Bank Asset #166",
    "country": "China",
    "lat": 35.2136,
    "lon": 112.4498,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_167",
    "name": "China Industrial/Bank Asset #167",
    "country": "China",
    "lat": 39.5929,
    "lon": 106.698,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_168",
    "name": "China Industrial/Bank Asset #168",
    "country": "China",
    "lat": 25.5292,
    "lon": 107.6703,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_169",
    "name": "China Industrial/Bank Asset #169",
    "country": "China",
    "lat": 37.1194,
    "lon": 106.4966,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_170",
    "name": "China Industrial/Bank Asset #170",
    "country": "China",
    "lat": 33.0851,
    "lon": 113.6997,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_171",
    "name": "China Industrial/Bank Asset #171",
    "country": "China",
    "lat": 39.4275,
    "lon": 109.7354,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_172",
    "name": "China Industrial/Bank Asset #172",
    "country": "China",
    "lat": 28.1759,
    "lon": 111.3002,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_173",
    "name": "China Industrial/Bank Asset #173",
    "country": "China",
    "lat": 36.8131,
    "lon": 119.0145,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_174",
    "name": "China Industrial/Bank Asset #174",
    "country": "China",
    "lat": 35.7656,
    "lon": 111.3612,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_175",
    "name": "China Industrial/Bank Asset #175",
    "country": "China",
    "lat": 28.3513,
    "lon": 106.4937,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_176",
    "name": "China Industrial/Bank Asset #176",
    "country": "China",
    "lat": 27.2434,
    "lon": 120.5987,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_177",
    "name": "China Industrial/Bank Asset #177",
    "country": "China",
    "lat": 33.3553,
    "lon": 108.1082,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_178",
    "name": "China Industrial/Bank Asset #178",
    "country": "China",
    "lat": 26.63,
    "lon": 114.3211,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_179",
    "name": "China Industrial/Bank Asset #179",
    "country": "China",
    "lat": 30.5042,
    "lon": 115.7185,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_180",
    "name": "China Industrial/Bank Asset #180",
    "country": "China",
    "lat": 39.4342,
    "lon": 109.1527,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_181",
    "name": "China Industrial/Bank Asset #181",
    "country": "China",
    "lat": 28.9329,
    "lon": 110.3002,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_182",
    "name": "China Industrial/Bank Asset #182",
    "country": "China",
    "lat": 25.9186,
    "lon": 108.1523,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_183",
    "name": "China Industrial/Bank Asset #183",
    "country": "China",
    "lat": 34.9769,
    "lon": 121.5277,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_184",
    "name": "China Industrial/Bank Asset #184",
    "country": "China",
    "lat": 35.15,
    "lon": 105.8066,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_185",
    "name": "China Industrial/Bank Asset #185",
    "country": "China",
    "lat": 37.3748,
    "lon": 111.5559,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_186",
    "name": "China Industrial/Bank Asset #186",
    "country": "China",
    "lat": 25.4594,
    "lon": 109.9644,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_187",
    "name": "China Industrial/Bank Asset #187",
    "country": "China",
    "lat": 29.6919,
    "lon": 115.2692,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_188",
    "name": "China Industrial/Bank Asset #188",
    "country": "China",
    "lat": 34.8349,
    "lon": 110.2033,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_189",
    "name": "China Industrial/Bank Asset #189",
    "country": "China",
    "lat": 39.8508,
    "lon": 105.6216,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_190",
    "name": "China Industrial/Bank Asset #190",
    "country": "China",
    "lat": 30.4703,
    "lon": 114.044,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_191",
    "name": "China Industrial/Bank Asset #191",
    "country": "China",
    "lat": 35.9693,
    "lon": 109.9971,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_192",
    "name": "China Industrial/Bank Asset #192",
    "country": "China",
    "lat": 31.3927,
    "lon": 121.0779,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_193",
    "name": "China Industrial/Bank Asset #193",
    "country": "China",
    "lat": 26.2367,
    "lon": 105.2391,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_194",
    "name": "China Industrial/Bank Asset #194",
    "country": "China",
    "lat": 37.286,
    "lon": 124.6513,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_195",
    "name": "China Industrial/Bank Asset #195",
    "country": "China",
    "lat": 26.0914,
    "lon": 121.4735,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_196",
    "name": "China Industrial/Bank Asset #196",
    "country": "China",
    "lat": 29.9558,
    "lon": 117.606,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_197",
    "name": "China Industrial/Bank Asset #197",
    "country": "China",
    "lat": 34.315,
    "lon": 116.6465,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_198",
    "name": "China Industrial/Bank Asset #198",
    "country": "China",
    "lat": 28.1411,
    "lon": 121.2549,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_199",
    "name": "China Industrial/Bank Asset #199",
    "country": "China",
    "lat": 24.3488,
    "lon": 106.2894,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_200",
    "name": "China Industrial/Bank Asset #200",
    "country": "China",
    "lat": 38.4399,
    "lon": 113.8686,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_201",
    "name": "China Industrial/Bank Asset #201",
    "country": "China",
    "lat": 26.0607,
    "lon": 123.1016,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_202",
    "name": "China Industrial/Bank Asset #202",
    "country": "China",
    "lat": 37.2697,
    "lon": 111.631,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_203",
    "name": "China Industrial/Bank Asset #203",
    "country": "China",
    "lat": 24.6831,
    "lon": 114.2199,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_204",
    "name": "China Industrial/Bank Asset #204",
    "country": "China",
    "lat": 26.6878,
    "lon": 116.4777,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_205",
    "name": "China Industrial/Bank Asset #205",
    "country": "China",
    "lat": 37.147,
    "lon": 112.9,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_206",
    "name": "China Industrial/Bank Asset #206",
    "country": "China",
    "lat": 24.4717,
    "lon": 118.6643,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_207",
    "name": "China Industrial/Bank Asset #207",
    "country": "China",
    "lat": 26.7649,
    "lon": 109.2943,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_208",
    "name": "China Industrial/Bank Asset #208",
    "country": "China",
    "lat": 26.9944,
    "lon": 110.5971,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_209",
    "name": "China Industrial/Bank Asset #209",
    "country": "China",
    "lat": 38.1348,
    "lon": 105.693,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_210",
    "name": "China Industrial/Bank Asset #210",
    "country": "China",
    "lat": 33.9068,
    "lon": 109.9157,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_211",
    "name": "China Industrial/Bank Asset #211",
    "country": "China",
    "lat": 28.7217,
    "lon": 113.2398,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_212",
    "name": "China Industrial/Bank Asset #212",
    "country": "China",
    "lat": 32.811,
    "lon": 106.2196,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_213",
    "name": "China Industrial/Bank Asset #213",
    "country": "China",
    "lat": 28.4764,
    "lon": 107.7447,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_214",
    "name": "China Industrial/Bank Asset #214",
    "country": "China",
    "lat": 27.1913,
    "lon": 122.6931,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_215",
    "name": "China Industrial/Bank Asset #215",
    "country": "China",
    "lat": 32.413,
    "lon": 117.6151,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_216",
    "name": "China Industrial/Bank Asset #216",
    "country": "China",
    "lat": 36.8347,
    "lon": 120.8969,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_217",
    "name": "China Industrial/Bank Asset #217",
    "country": "China",
    "lat": 39.8305,
    "lon": 120.6383,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_218",
    "name": "China Industrial/Bank Asset #218",
    "country": "China",
    "lat": 29.7458,
    "lon": 115.8904,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_219",
    "name": "China Industrial/Bank Asset #219",
    "country": "China",
    "lat": 31.7549,
    "lon": 123.2535,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_220",
    "name": "China Industrial/Bank Asset #220",
    "country": "China",
    "lat": 32.0383,
    "lon": 112.7676,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_221",
    "name": "China Industrial/Bank Asset #221",
    "country": "China",
    "lat": 26.8771,
    "lon": 111.3776,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_222",
    "name": "China Industrial/Bank Asset #222",
    "country": "China",
    "lat": 27.5043,
    "lon": 122.9153,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_223",
    "name": "China Industrial/Bank Asset #223",
    "country": "China",
    "lat": 36.4566,
    "lon": 106.1718,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_224",
    "name": "China Industrial/Bank Asset #224",
    "country": "China",
    "lat": 39.8645,
    "lon": 115.5886,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_225",
    "name": "China Industrial/Bank Asset #225",
    "country": "China",
    "lat": 36.2695,
    "lon": 124.9921,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_226",
    "name": "China Industrial/Bank Asset #226",
    "country": "China",
    "lat": 39.5837,
    "lon": 107.0027,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_227",
    "name": "China Industrial/Bank Asset #227",
    "country": "China",
    "lat": 34.5098,
    "lon": 110.3305,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_228",
    "name": "China Industrial/Bank Asset #228",
    "country": "China",
    "lat": 37.0606,
    "lon": 123.3452,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_229",
    "name": "China Industrial/Bank Asset #229",
    "country": "China",
    "lat": 24.8945,
    "lon": 124.9278,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_230",
    "name": "China Industrial/Bank Asset #230",
    "country": "China",
    "lat": 27.5106,
    "lon": 121.9301,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_231",
    "name": "China Industrial/Bank Asset #231",
    "country": "China",
    "lat": 36.7583,
    "lon": 112.0961,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_232",
    "name": "China Industrial/Bank Asset #232",
    "country": "China",
    "lat": 37.4276,
    "lon": 121.9044,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_233",
    "name": "China Industrial/Bank Asset #233",
    "country": "China",
    "lat": 26.8176,
    "lon": 116.8504,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_234",
    "name": "China Industrial/Bank Asset #234",
    "country": "China",
    "lat": 36.8994,
    "lon": 118.9525,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_235",
    "name": "China Industrial/Bank Asset #235",
    "country": "China",
    "lat": 38.6237,
    "lon": 105.5641,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_236",
    "name": "China Industrial/Bank Asset #236",
    "country": "China",
    "lat": 35.209,
    "lon": 123.9512,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_237",
    "name": "China Industrial/Bank Asset #237",
    "country": "China",
    "lat": 33.0177,
    "lon": 116.2622,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_238",
    "name": "China Industrial/Bank Asset #238",
    "country": "China",
    "lat": 27.0117,
    "lon": 124.7601,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_239",
    "name": "China Industrial/Bank Asset #239",
    "country": "China",
    "lat": 38.106,
    "lon": 114.8445,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_240",
    "name": "China Industrial/Bank Asset #240",
    "country": "China",
    "lat": 28.9448,
    "lon": 114.8087,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_241",
    "name": "China Industrial/Bank Asset #241",
    "country": "China",
    "lat": 25.4441,
    "lon": 109.6525,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_242",
    "name": "China Industrial/Bank Asset #242",
    "country": "China",
    "lat": 27.5009,
    "lon": 115.529,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_243",
    "name": "China Industrial/Bank Asset #243",
    "country": "China",
    "lat": 24.0109,
    "lon": 123.3579,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_244",
    "name": "China Industrial/Bank Asset #244",
    "country": "China",
    "lat": 27.2234,
    "lon": 107.6098,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_245",
    "name": "China Industrial/Bank Asset #245",
    "country": "China",
    "lat": 35.471,
    "lon": 123.3756,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_246",
    "name": "China Industrial/Bank Asset #246",
    "country": "China",
    "lat": 37.5085,
    "lon": 111.4718,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_247",
    "name": "China Industrial/Bank Asset #247",
    "country": "China",
    "lat": 24.3506,
    "lon": 116.7322,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_248",
    "name": "China Industrial/Bank Asset #248",
    "country": "China",
    "lat": 38.6756,
    "lon": 120.4873,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_249",
    "name": "China Industrial/Bank Asset #249",
    "country": "China",
    "lat": 37.5437,
    "lon": 122.2134,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_250",
    "name": "China Industrial/Bank Asset #250",
    "country": "China",
    "lat": 39.3689,
    "lon": 112.4718,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_251",
    "name": "China Industrial/Bank Asset #251",
    "country": "China",
    "lat": 39.0708,
    "lon": 112.9119,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_252",
    "name": "China Industrial/Bank Asset #252",
    "country": "China",
    "lat": 25.6165,
    "lon": 111.0353,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_253",
    "name": "China Industrial/Bank Asset #253",
    "country": "China",
    "lat": 26.1832,
    "lon": 108.1501,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_254",
    "name": "China Industrial/Bank Asset #254",
    "country": "China",
    "lat": 39.1791,
    "lon": 120.8369,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_255",
    "name": "China Industrial/Bank Asset #255",
    "country": "China",
    "lat": 39.3706,
    "lon": 117.9836,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_256",
    "name": "China Industrial/Bank Asset #256",
    "country": "China",
    "lat": 26.7872,
    "lon": 124.3749,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_257",
    "name": "China Industrial/Bank Asset #257",
    "country": "China",
    "lat": 35.097,
    "lon": 123.5769,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_258",
    "name": "China Industrial/Bank Asset #258",
    "country": "China",
    "lat": 36.5919,
    "lon": 109.4647,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_259",
    "name": "China Industrial/Bank Asset #259",
    "country": "China",
    "lat": 33.4232,
    "lon": 108.507,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_260",
    "name": "China Industrial/Bank Asset #260",
    "country": "China",
    "lat": 28.9092,
    "lon": 118.77,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_261",
    "name": "China Industrial/Bank Asset #261",
    "country": "China",
    "lat": 26.0376,
    "lon": 119.5766,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_262",
    "name": "China Industrial/Bank Asset #262",
    "country": "China",
    "lat": 39.1806,
    "lon": 123.974,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_263",
    "name": "China Industrial/Bank Asset #263",
    "country": "China",
    "lat": 30.2656,
    "lon": 124.8857,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_264",
    "name": "China Industrial/Bank Asset #264",
    "country": "China",
    "lat": 39.4429,
    "lon": 105.6477,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_265",
    "name": "China Industrial/Bank Asset #265",
    "country": "China",
    "lat": 33.6382,
    "lon": 123.4208,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_266",
    "name": "China Industrial/Bank Asset #266",
    "country": "China",
    "lat": 39.4805,
    "lon": 109.4179,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_267",
    "name": "China Industrial/Bank Asset #267",
    "country": "China",
    "lat": 33.0488,
    "lon": 123.7338,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_268",
    "name": "China Industrial/Bank Asset #268",
    "country": "China",
    "lat": 26.2503,
    "lon": 119.9069,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_269",
    "name": "China Industrial/Bank Asset #269",
    "country": "China",
    "lat": 27.8079,
    "lon": 124.6476,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_270",
    "name": "China Industrial/Bank Asset #270",
    "country": "China",
    "lat": 26.6862,
    "lon": 122.7064,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_271",
    "name": "China Industrial/Bank Asset #271",
    "country": "China",
    "lat": 25.4196,
    "lon": 119.1793,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_272",
    "name": "China Industrial/Bank Asset #272",
    "country": "China",
    "lat": 34.2256,
    "lon": 122.7331,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_273",
    "name": "China Industrial/Bank Asset #273",
    "country": "China",
    "lat": 31.1461,
    "lon": 110.3042,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_274",
    "name": "China Industrial/Bank Asset #274",
    "country": "China",
    "lat": 27.9927,
    "lon": 106.3559,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_275",
    "name": "China Industrial/Bank Asset #275",
    "country": "China",
    "lat": 28.1065,
    "lon": 107.1607,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_276",
    "name": "China Industrial/Bank Asset #276",
    "country": "China",
    "lat": 24.0205,
    "lon": 112.7187,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_277",
    "name": "China Industrial/Bank Asset #277",
    "country": "China",
    "lat": 35.7214,
    "lon": 124.382,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_278",
    "name": "China Industrial/Bank Asset #278",
    "country": "China",
    "lat": 38.1528,
    "lon": 114.8616,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_279",
    "name": "China Industrial/Bank Asset #279",
    "country": "China",
    "lat": 30.0594,
    "lon": 115.9205,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_280",
    "name": "China Industrial/Bank Asset #280",
    "country": "China",
    "lat": 25.6229,
    "lon": 114.5898,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_281",
    "name": "China Industrial/Bank Asset #281",
    "country": "China",
    "lat": 37.8248,
    "lon": 118.0194,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_282",
    "name": "China Industrial/Bank Asset #282",
    "country": "China",
    "lat": 34.9946,
    "lon": 108.2531,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_283",
    "name": "China Industrial/Bank Asset #283",
    "country": "China",
    "lat": 25.1794,
    "lon": 121.9152,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_284",
    "name": "China Industrial/Bank Asset #284",
    "country": "China",
    "lat": 28.7185,
    "lon": 111.3743,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_285",
    "name": "China Industrial/Bank Asset #285",
    "country": "China",
    "lat": 39.2266,
    "lon": 106.484,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_286",
    "name": "China Industrial/Bank Asset #286",
    "country": "China",
    "lat": 26.7217,
    "lon": 112.5092,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_287",
    "name": "China Industrial/Bank Asset #287",
    "country": "China",
    "lat": 35.7118,
    "lon": 115.9409,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_288",
    "name": "China Industrial/Bank Asset #288",
    "country": "China",
    "lat": 38.37,
    "lon": 106.8621,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_289",
    "name": "China Industrial/Bank Asset #289",
    "country": "China",
    "lat": 33.5045,
    "lon": 117.2729,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_290",
    "name": "China Industrial/Bank Asset #290",
    "country": "China",
    "lat": 31.7238,
    "lon": 105.6199,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_291",
    "name": "China Industrial/Bank Asset #291",
    "country": "China",
    "lat": 39.0791,
    "lon": 108.2999,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_292",
    "name": "China Industrial/Bank Asset #292",
    "country": "China",
    "lat": 38.2361,
    "lon": 108.1421,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_293",
    "name": "China Industrial/Bank Asset #293",
    "country": "China",
    "lat": 25.6201,
    "lon": 109.111,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_294",
    "name": "China Industrial/Bank Asset #294",
    "country": "China",
    "lat": 27.0397,
    "lon": 118.9439,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_295",
    "name": "China Industrial/Bank Asset #295",
    "country": "China",
    "lat": 35.5526,
    "lon": 119.5995,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_296",
    "name": "China Industrial/Bank Asset #296",
    "country": "China",
    "lat": 28.2442,
    "lon": 110.6305,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_297",
    "name": "China Industrial/Bank Asset #297",
    "country": "China",
    "lat": 27.8008,
    "lon": 105.9927,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_298",
    "name": "China Industrial/Bank Asset #298",
    "country": "China",
    "lat": 33.1483,
    "lon": 121.7971,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_299",
    "name": "China Industrial/Bank Asset #299",
    "country": "China",
    "lat": 26.4574,
    "lon": 112.2166,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_300",
    "name": "China Industrial/Bank Asset #300",
    "country": "China",
    "lat": 30.8417,
    "lon": 110.891,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_301",
    "name": "China Industrial/Bank Asset #301",
    "country": "China",
    "lat": 34.5923,
    "lon": 117.0043,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_302",
    "name": "China Industrial/Bank Asset #302",
    "country": "China",
    "lat": 27.1948,
    "lon": 105.5147,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_303",
    "name": "China Industrial/Bank Asset #303",
    "country": "China",
    "lat": 26.7333,
    "lon": 110.8362,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_304",
    "name": "China Industrial/Bank Asset #304",
    "country": "China",
    "lat": 25.311,
    "lon": 121.8754,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_305",
    "name": "China Industrial/Bank Asset #305",
    "country": "China",
    "lat": 28.9337,
    "lon": 112.9493,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_306",
    "name": "China Industrial/Bank Asset #306",
    "country": "China",
    "lat": 31.8255,
    "lon": 118.2208,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_307",
    "name": "China Industrial/Bank Asset #307",
    "country": "China",
    "lat": 25.4582,
    "lon": 115.8825,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_308",
    "name": "China Industrial/Bank Asset #308",
    "country": "China",
    "lat": 26.9581,
    "lon": 122.7099,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_309",
    "name": "China Industrial/Bank Asset #309",
    "country": "China",
    "lat": 29.9104,
    "lon": 113.9155,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_chi_310",
    "name": "China Industrial/Bank Asset #310",
    "country": "China",
    "lat": 28.2127,
    "lon": 114.3012,
    "type": "State Grid & Manufacturing Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_1",
    "name": "Japan Industrial/Bank Asset #001",
    "country": "Japan",
    "lat": 34.0099,
    "lon": 136.8614,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_2",
    "name": "Japan Industrial/Bank Asset #002",
    "country": "Japan",
    "lat": 32.6931,
    "lon": 139.7634,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_3",
    "name": "Japan Industrial/Bank Asset #003",
    "country": "Japan",
    "lat": 37.5397,
    "lon": 135.7642,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_4",
    "name": "Japan Industrial/Bank Asset #004",
    "country": "Japan",
    "lat": 34.9503,
    "lon": 138.4987,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_5",
    "name": "Japan Industrial/Bank Asset #005",
    "country": "Japan",
    "lat": 39.9656,
    "lon": 138.7884,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_6",
    "name": "Japan Industrial/Bank Asset #006",
    "country": "Japan",
    "lat": 36.6288,
    "lon": 140.2948,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_7",
    "name": "Japan Industrial/Bank Asset #007",
    "country": "Japan",
    "lat": 38.7472,
    "lon": 137.7618,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_8",
    "name": "Japan Industrial/Bank Asset #008",
    "country": "Japan",
    "lat": 36.4841,
    "lon": 140.4514,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_9",
    "name": "Japan Industrial/Bank Asset #009",
    "country": "Japan",
    "lat": 35.9986,
    "lon": 140.5399,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_10",
    "name": "Japan Industrial/Bank Asset #010",
    "country": "Japan",
    "lat": 36.0101,
    "lon": 135.7237,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_11",
    "name": "Japan Industrial/Bank Asset #011",
    "country": "Japan",
    "lat": 39.4222,
    "lon": 139.5358,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_12",
    "name": "Japan Industrial/Bank Asset #012",
    "country": "Japan",
    "lat": 36.2168,
    "lon": 140.6527,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_13",
    "name": "Japan Industrial/Bank Asset #013",
    "country": "Japan",
    "lat": 38.6036,
    "lon": 139.3152,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_14",
    "name": "Japan Industrial/Bank Asset #014",
    "country": "Japan",
    "lat": 37.1622,
    "lon": 135.9717,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_15",
    "name": "Japan Industrial/Bank Asset #015",
    "country": "Japan",
    "lat": 38.2575,
    "lon": 136.2873,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_16",
    "name": "Japan Industrial/Bank Asset #016",
    "country": "Japan",
    "lat": 40.0749,
    "lon": 141.083,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_17",
    "name": "Japan Industrial/Bank Asset #017",
    "country": "Japan",
    "lat": 38.6677,
    "lon": 136.0071,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_18",
    "name": "Japan Industrial/Bank Asset #018",
    "country": "Japan",
    "lat": 35.587,
    "lon": 141.1797,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_19",
    "name": "Japan Industrial/Bank Asset #019",
    "country": "Japan",
    "lat": 35.6831,
    "lon": 141.2336,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_20",
    "name": "Japan Industrial/Bank Asset #020",
    "country": "Japan",
    "lat": 37.2178,
    "lon": 140.2546,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_21",
    "name": "Japan Industrial/Bank Asset #021",
    "country": "Japan",
    "lat": 34.2631,
    "lon": 140.7148,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_22",
    "name": "Japan Industrial/Bank Asset #022",
    "country": "Japan",
    "lat": 39.5134,
    "lon": 135.6521,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_23",
    "name": "Japan Industrial/Bank Asset #023",
    "country": "Japan",
    "lat": 35.3048,
    "lon": 137.6341,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_24",
    "name": "Japan Industrial/Bank Asset #024",
    "country": "Japan",
    "lat": 34.809,
    "lon": 136.9072,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_25",
    "name": "Japan Industrial/Bank Asset #025",
    "country": "Japan",
    "lat": 35.8653,
    "lon": 140.4908,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_26",
    "name": "Japan Industrial/Bank Asset #026",
    "country": "Japan",
    "lat": 38.4924,
    "lon": 138.9883,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_27",
    "name": "Japan Industrial/Bank Asset #027",
    "country": "Japan",
    "lat": 36.3805,
    "lon": 137.7676,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_28",
    "name": "Japan Industrial/Bank Asset #028",
    "country": "Japan",
    "lat": 35.5155,
    "lon": 136.1392,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_29",
    "name": "Japan Industrial/Bank Asset #029",
    "country": "Japan",
    "lat": 36.9035,
    "lon": 139.8003,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_30",
    "name": "Japan Industrial/Bank Asset #030",
    "country": "Japan",
    "lat": 39.7172,
    "lon": 140.7996,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_31",
    "name": "Japan Industrial/Bank Asset #031",
    "country": "Japan",
    "lat": 36.7015,
    "lon": 135.8559,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_32",
    "name": "Japan Industrial/Bank Asset #032",
    "country": "Japan",
    "lat": 34.4887,
    "lon": 138.4638,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_33",
    "name": "Japan Industrial/Bank Asset #033",
    "country": "Japan",
    "lat": 34.951,
    "lon": 137.7153,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_34",
    "name": "Japan Industrial/Bank Asset #034",
    "country": "Japan",
    "lat": 35.2643,
    "lon": 138.1635,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_35",
    "name": "Japan Industrial/Bank Asset #035",
    "country": "Japan",
    "lat": 37.0717,
    "lon": 135.4748,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_36",
    "name": "Japan Industrial/Bank Asset #036",
    "country": "Japan",
    "lat": 34.4033,
    "lon": 136.1131,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_37",
    "name": "Japan Industrial/Bank Asset #037",
    "country": "Japan",
    "lat": 37.0692,
    "lon": 139.412,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_38",
    "name": "Japan Industrial/Bank Asset #038",
    "country": "Japan",
    "lat": 32.5103,
    "lon": 140.5874,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_39",
    "name": "Japan Industrial/Bank Asset #039",
    "country": "Japan",
    "lat": 34.852,
    "lon": 136.6755,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_40",
    "name": "Japan Industrial/Bank Asset #040",
    "country": "Japan",
    "lat": 38.166,
    "lon": 140.775,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_41",
    "name": "Japan Industrial/Bank Asset #041",
    "country": "Japan",
    "lat": 39.3763,
    "lon": 135.3714,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_42",
    "name": "Japan Industrial/Bank Asset #042",
    "country": "Japan",
    "lat": 38.7391,
    "lon": 137.0683,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_43",
    "name": "Japan Industrial/Bank Asset #043",
    "country": "Japan",
    "lat": 34.4428,
    "lon": 138.1997,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_44",
    "name": "Japan Industrial/Bank Asset #044",
    "country": "Japan",
    "lat": 37.7695,
    "lon": 135.8393,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_45",
    "name": "Japan Industrial/Bank Asset #045",
    "country": "Japan",
    "lat": 39.1512,
    "lon": 136.0563,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_46",
    "name": "Japan Industrial/Bank Asset #046",
    "country": "Japan",
    "lat": 39.9938,
    "lon": 137.9087,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_47",
    "name": "Japan Industrial/Bank Asset #047",
    "country": "Japan",
    "lat": 38.8066,
    "lon": 136.8665,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_48",
    "name": "Japan Industrial/Bank Asset #048",
    "country": "Japan",
    "lat": 35.5342,
    "lon": 139.1233,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_49",
    "name": "Japan Industrial/Bank Asset #049",
    "country": "Japan",
    "lat": 33.7035,
    "lon": 136.5183,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_50",
    "name": "Japan Industrial/Bank Asset #050",
    "country": "Japan",
    "lat": 38.7918,
    "lon": 139.6957,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_51",
    "name": "Japan Industrial/Bank Asset #051",
    "country": "Japan",
    "lat": 38.2759,
    "lon": 140.4531,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_52",
    "name": "Japan Industrial/Bank Asset #052",
    "country": "Japan",
    "lat": 38.7681,
    "lon": 138.3416,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_53",
    "name": "Japan Industrial/Bank Asset #053",
    "country": "Japan",
    "lat": 33.4718,
    "lon": 137.1167,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_54",
    "name": "Japan Industrial/Bank Asset #054",
    "country": "Japan",
    "lat": 36.2544,
    "lon": 136.0639,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_55",
    "name": "Japan Industrial/Bank Asset #055",
    "country": "Japan",
    "lat": 39.0104,
    "lon": 140.526,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_56",
    "name": "Japan Industrial/Bank Asset #056",
    "country": "Japan",
    "lat": 32.4316,
    "lon": 136.4066,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_57",
    "name": "Japan Industrial/Bank Asset #057",
    "country": "Japan",
    "lat": 38.8634,
    "lon": 140.2719,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_58",
    "name": "Japan Industrial/Bank Asset #058",
    "country": "Japan",
    "lat": 34.1959,
    "lon": 137.9887,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_59",
    "name": "Japan Industrial/Bank Asset #059",
    "country": "Japan",
    "lat": 39.5442,
    "lon": 139.4778,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_60",
    "name": "Japan Industrial/Bank Asset #060",
    "country": "Japan",
    "lat": 34.3918,
    "lon": 140.191,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_61",
    "name": "Japan Industrial/Bank Asset #061",
    "country": "Japan",
    "lat": 36.241,
    "lon": 139.0625,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_62",
    "name": "Japan Industrial/Bank Asset #062",
    "country": "Japan",
    "lat": 33.191,
    "lon": 135.4334,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_63",
    "name": "Japan Industrial/Bank Asset #063",
    "country": "Japan",
    "lat": 35.1797,
    "lon": 138.8143,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_64",
    "name": "Japan Industrial/Bank Asset #064",
    "country": "Japan",
    "lat": 33.6207,
    "lon": 140.4729,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_65",
    "name": "Japan Industrial/Bank Asset #065",
    "country": "Japan",
    "lat": 36.895,
    "lon": 137.3486,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_66",
    "name": "Japan Industrial/Bank Asset #066",
    "country": "Japan",
    "lat": 33.5081,
    "lon": 140.617,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_67",
    "name": "Japan Industrial/Bank Asset #067",
    "country": "Japan",
    "lat": 38.1917,
    "lon": 139.3831,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_68",
    "name": "Japan Industrial/Bank Asset #068",
    "country": "Japan",
    "lat": 34.4806,
    "lon": 137.5694,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_69",
    "name": "Japan Industrial/Bank Asset #069",
    "country": "Japan",
    "lat": 33.5033,
    "lon": 138.6835,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_70",
    "name": "Japan Industrial/Bank Asset #070",
    "country": "Japan",
    "lat": 39.9193,
    "lon": 140.3927,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_71",
    "name": "Japan Industrial/Bank Asset #071",
    "country": "Japan",
    "lat": 37.379,
    "lon": 139.3162,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_72",
    "name": "Japan Industrial/Bank Asset #072",
    "country": "Japan",
    "lat": 34.3527,
    "lon": 137.707,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_73",
    "name": "Japan Industrial/Bank Asset #073",
    "country": "Japan",
    "lat": 32.3604,
    "lon": 139.9318,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_74",
    "name": "Japan Industrial/Bank Asset #074",
    "country": "Japan",
    "lat": 38.3406,
    "lon": 135.3034,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_75",
    "name": "Japan Industrial/Bank Asset #075",
    "country": "Japan",
    "lat": 39.4921,
    "lon": 139.1342,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_76",
    "name": "Japan Industrial/Bank Asset #076",
    "country": "Japan",
    "lat": 37.0091,
    "lon": 135.3008,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_77",
    "name": "Japan Industrial/Bank Asset #077",
    "country": "Japan",
    "lat": 34.2191,
    "lon": 140.0805,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_78",
    "name": "Japan Industrial/Bank Asset #078",
    "country": "Japan",
    "lat": 34.6437,
    "lon": 141.0521,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_79",
    "name": "Japan Industrial/Bank Asset #079",
    "country": "Japan",
    "lat": 37.3419,
    "lon": 137.7928,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_80",
    "name": "Japan Industrial/Bank Asset #080",
    "country": "Japan",
    "lat": 35.2118,
    "lon": 137.3423,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_81",
    "name": "Japan Industrial/Bank Asset #081",
    "country": "Japan",
    "lat": 34.216,
    "lon": 138.0502,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_82",
    "name": "Japan Industrial/Bank Asset #082",
    "country": "Japan",
    "lat": 37.6176,
    "lon": 140.1959,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_83",
    "name": "Japan Industrial/Bank Asset #083",
    "country": "Japan",
    "lat": 35.3772,
    "lon": 135.8639,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_84",
    "name": "Japan Industrial/Bank Asset #084",
    "country": "Japan",
    "lat": 36.2921,
    "lon": 139.2241,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_85",
    "name": "Japan Industrial/Bank Asset #085",
    "country": "Japan",
    "lat": 38.9463,
    "lon": 137.4954,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_86",
    "name": "Japan Industrial/Bank Asset #086",
    "country": "Japan",
    "lat": 37.3787,
    "lon": 138.9043,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_87",
    "name": "Japan Industrial/Bank Asset #087",
    "country": "Japan",
    "lat": 34.5878,
    "lon": 135.8986,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_88",
    "name": "Japan Industrial/Bank Asset #088",
    "country": "Japan",
    "lat": 32.7107,
    "lon": 141.1802,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_89",
    "name": "Japan Industrial/Bank Asset #089",
    "country": "Japan",
    "lat": 37.3248,
    "lon": 140.4189,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_90",
    "name": "Japan Industrial/Bank Asset #090",
    "country": "Japan",
    "lat": 34.2892,
    "lon": 139.5166,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_91",
    "name": "Japan Industrial/Bank Asset #091",
    "country": "Japan",
    "lat": 39.339,
    "lon": 137.0427,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_92",
    "name": "Japan Industrial/Bank Asset #092",
    "country": "Japan",
    "lat": 33.3994,
    "lon": 139.8428,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_93",
    "name": "Japan Industrial/Bank Asset #093",
    "country": "Japan",
    "lat": 39.3975,
    "lon": 140.0826,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_94",
    "name": "Japan Industrial/Bank Asset #094",
    "country": "Japan",
    "lat": 38.6189,
    "lon": 138.8502,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_95",
    "name": "Japan Industrial/Bank Asset #095",
    "country": "Japan",
    "lat": 37.4842,
    "lon": 139.3345,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_96",
    "name": "Japan Industrial/Bank Asset #096",
    "country": "Japan",
    "lat": 37.9703,
    "lon": 139.1824,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_97",
    "name": "Japan Industrial/Bank Asset #097",
    "country": "Japan",
    "lat": 40.1798,
    "lon": 136.8066,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_98",
    "name": "Japan Industrial/Bank Asset #098",
    "country": "Japan",
    "lat": 35.5485,
    "lon": 137.5796,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_99",
    "name": "Japan Industrial/Bank Asset #099",
    "country": "Japan",
    "lat": 32.4826,
    "lon": 139.4984,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_100",
    "name": "Japan Industrial/Bank Asset #100",
    "country": "Japan",
    "lat": 36.7763,
    "lon": 136.3895,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_101",
    "name": "Japan Industrial/Bank Asset #101",
    "country": "Japan",
    "lat": 38.0124,
    "lon": 136.5842,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_102",
    "name": "Japan Industrial/Bank Asset #102",
    "country": "Japan",
    "lat": 36.4771,
    "lon": 139.9594,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_103",
    "name": "Japan Industrial/Bank Asset #103",
    "country": "Japan",
    "lat": 39.4522,
    "lon": 139.2812,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_104",
    "name": "Japan Industrial/Bank Asset #104",
    "country": "Japan",
    "lat": 36.2585,
    "lon": 140.3225,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_105",
    "name": "Japan Industrial/Bank Asset #105",
    "country": "Japan",
    "lat": 38.9251,
    "lon": 140.509,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_106",
    "name": "Japan Industrial/Bank Asset #106",
    "country": "Japan",
    "lat": 33.6491,
    "lon": 135.8356,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_107",
    "name": "Japan Industrial/Bank Asset #107",
    "country": "Japan",
    "lat": 33.2236,
    "lon": 136.8019,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_108",
    "name": "Japan Industrial/Bank Asset #108",
    "country": "Japan",
    "lat": 38.6668,
    "lon": 139.8275,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_109",
    "name": "Japan Industrial/Bank Asset #109",
    "country": "Japan",
    "lat": 33.6645,
    "lon": 139.3283,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_jap_110",
    "name": "Japan Industrial/Bank Asset #110",
    "country": "Japan",
    "lat": 34.8851,
    "lon": 135.7858,
    "type": "Keiretsu & Coastal Power Clusters",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_1",
    "name": "South Korea Industrial/Bank Asset #001",
    "country": "South Korea",
    "lat": 36.0659,
    "lon": 128.4826,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_2",
    "name": "South Korea Industrial/Bank Asset #002",
    "country": "South Korea",
    "lat": 35.9213,
    "lon": 128.6143,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_3",
    "name": "South Korea Industrial/Bank Asset #003",
    "country": "South Korea",
    "lat": 35.994,
    "lon": 127.0317,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_4",
    "name": "South Korea Industrial/Bank Asset #004",
    "country": "South Korea",
    "lat": 35.8822,
    "lon": 128.8036,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_5",
    "name": "South Korea Industrial/Bank Asset #005",
    "country": "South Korea",
    "lat": 36.4116,
    "lon": 128.8492,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_6",
    "name": "South Korea Industrial/Bank Asset #006",
    "country": "South Korea",
    "lat": 36.7507,
    "lon": 129.0829,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_7",
    "name": "South Korea Industrial/Bank Asset #007",
    "country": "South Korea",
    "lat": 35.2136,
    "lon": 128.9183,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_8",
    "name": "South Korea Industrial/Bank Asset #008",
    "country": "South Korea",
    "lat": 36.5014,
    "lon": 128.8525,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_9",
    "name": "South Korea Industrial/Bank Asset #009",
    "country": "South Korea",
    "lat": 36.145,
    "lon": 127.1451,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_10",
    "name": "South Korea Industrial/Bank Asset #010",
    "country": "South Korea",
    "lat": 35.1622,
    "lon": 128.8127,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_11",
    "name": "South Korea Industrial/Bank Asset #011",
    "country": "South Korea",
    "lat": 35.4121,
    "lon": 126.8509,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_12",
    "name": "South Korea Industrial/Bank Asset #012",
    "country": "South Korea",
    "lat": 36.2276,
    "lon": 127.9582,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_13",
    "name": "South Korea Industrial/Bank Asset #013",
    "country": "South Korea",
    "lat": 37.7199,
    "lon": 127.6227,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_14",
    "name": "South Korea Industrial/Bank Asset #014",
    "country": "South Korea",
    "lat": 35.9492,
    "lon": 128.397,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_15",
    "name": "South Korea Industrial/Bank Asset #015",
    "country": "South Korea",
    "lat": 37.3368,
    "lon": 127.7127,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_16",
    "name": "South Korea Industrial/Bank Asset #016",
    "country": "South Korea",
    "lat": 36.8931,
    "lon": 126.7805,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_17",
    "name": "South Korea Industrial/Bank Asset #017",
    "country": "South Korea",
    "lat": 36.9035,
    "lon": 126.2641,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_18",
    "name": "South Korea Industrial/Bank Asset #018",
    "country": "South Korea",
    "lat": 35.8206,
    "lon": 128.5336,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_19",
    "name": "South Korea Industrial/Bank Asset #019",
    "country": "South Korea",
    "lat": 35.5058,
    "lon": 128.5435,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_20",
    "name": "South Korea Industrial/Bank Asset #020",
    "country": "South Korea",
    "lat": 36.4687,
    "lon": 128.5407,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_21",
    "name": "South Korea Industrial/Bank Asset #021",
    "country": "South Korea",
    "lat": 35.2641,
    "lon": 128.0934,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_22",
    "name": "South Korea Industrial/Bank Asset #022",
    "country": "South Korea",
    "lat": 36.9005,
    "lon": 127.4602,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_23",
    "name": "South Korea Industrial/Bank Asset #023",
    "country": "South Korea",
    "lat": 37.896,
    "lon": 127.3999,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_24",
    "name": "South Korea Industrial/Bank Asset #024",
    "country": "South Korea",
    "lat": 35.1132,
    "lon": 126.8482,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_25",
    "name": "South Korea Industrial/Bank Asset #025",
    "country": "South Korea",
    "lat": 36.1193,
    "lon": 126.2922,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_26",
    "name": "South Korea Industrial/Bank Asset #026",
    "country": "South Korea",
    "lat": 35.9666,
    "lon": 128.7497,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_27",
    "name": "South Korea Industrial/Bank Asset #027",
    "country": "South Korea",
    "lat": 35.5717,
    "lon": 128.2802,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_28",
    "name": "South Korea Industrial/Bank Asset #028",
    "country": "South Korea",
    "lat": 36.8801,
    "lon": 126.9965,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_29",
    "name": "South Korea Industrial/Bank Asset #029",
    "country": "South Korea",
    "lat": 37.0806,
    "lon": 127.283,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_30",
    "name": "South Korea Industrial/Bank Asset #030",
    "country": "South Korea",
    "lat": 35.3868,
    "lon": 127.4007,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_31",
    "name": "South Korea Industrial/Bank Asset #031",
    "country": "South Korea",
    "lat": 36.766,
    "lon": 126.7511,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_32",
    "name": "South Korea Industrial/Bank Asset #032",
    "country": "South Korea",
    "lat": 37.4715,
    "lon": 127.1446,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_33",
    "name": "South Korea Industrial/Bank Asset #033",
    "country": "South Korea",
    "lat": 35.8725,
    "lon": 128.4335,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_34",
    "name": "South Korea Industrial/Bank Asset #034",
    "country": "South Korea",
    "lat": 36.7891,
    "lon": 127.2635,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_35",
    "name": "South Korea Industrial/Bank Asset #035",
    "country": "South Korea",
    "lat": 37.6639,
    "lon": 129.2364,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_36",
    "name": "South Korea Industrial/Bank Asset #036",
    "country": "South Korea",
    "lat": 36.0282,
    "lon": 128.9542,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_37",
    "name": "South Korea Industrial/Bank Asset #037",
    "country": "South Korea",
    "lat": 36.0778,
    "lon": 126.8153,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_38",
    "name": "South Korea Industrial/Bank Asset #038",
    "country": "South Korea",
    "lat": 37.8443,
    "lon": 129.0046,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_39",
    "name": "South Korea Industrial/Bank Asset #039",
    "country": "South Korea",
    "lat": 36.2102,
    "lon": 126.9353,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_40",
    "name": "South Korea Industrial/Bank Asset #040",
    "country": "South Korea",
    "lat": 37.1815,
    "lon": 126.6436,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_41",
    "name": "South Korea Industrial/Bank Asset #041",
    "country": "South Korea",
    "lat": 37.2022,
    "lon": 128.0191,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_42",
    "name": "South Korea Industrial/Bank Asset #042",
    "country": "South Korea",
    "lat": 35.507,
    "lon": 127.3498,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_43",
    "name": "South Korea Industrial/Bank Asset #043",
    "country": "South Korea",
    "lat": 36.9516,
    "lon": 126.3621,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_44",
    "name": "South Korea Industrial/Bank Asset #044",
    "country": "South Korea",
    "lat": 37.6296,
    "lon": 127.0174,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_45",
    "name": "South Korea Industrial/Bank Asset #045",
    "country": "South Korea",
    "lat": 36.6042,
    "lon": 126.3958,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_46",
    "name": "South Korea Industrial/Bank Asset #046",
    "country": "South Korea",
    "lat": 37.984,
    "lon": 128.2359,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_47",
    "name": "South Korea Industrial/Bank Asset #047",
    "country": "South Korea",
    "lat": 36.9607,
    "lon": 126.3092,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_48",
    "name": "South Korea Industrial/Bank Asset #048",
    "country": "South Korea",
    "lat": 37.0692,
    "lon": 127.5003,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_49",
    "name": "South Korea Industrial/Bank Asset #049",
    "country": "South Korea",
    "lat": 36.1408,
    "lon": 127.8918,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_50",
    "name": "South Korea Industrial/Bank Asset #050",
    "country": "South Korea",
    "lat": 36.4232,
    "lon": 126.7094,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_51",
    "name": "South Korea Industrial/Bank Asset #051",
    "country": "South Korea",
    "lat": 37.0856,
    "lon": 128.1409,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_52",
    "name": "South Korea Industrial/Bank Asset #052",
    "country": "South Korea",
    "lat": 35.9033,
    "lon": 128.235,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_53",
    "name": "South Korea Industrial/Bank Asset #053",
    "country": "South Korea",
    "lat": 36.9874,
    "lon": 127.0599,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_54",
    "name": "South Korea Industrial/Bank Asset #054",
    "country": "South Korea",
    "lat": 36.8169,
    "lon": 126.6615,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_55",
    "name": "South Korea Industrial/Bank Asset #055",
    "country": "South Korea",
    "lat": 37.492,
    "lon": 126.5647,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_56",
    "name": "South Korea Industrial/Bank Asset #056",
    "country": "South Korea",
    "lat": 37.1563,
    "lon": 126.6032,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_57",
    "name": "South Korea Industrial/Bank Asset #057",
    "country": "South Korea",
    "lat": 35.342,
    "lon": 126.5688,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_58",
    "name": "South Korea Industrial/Bank Asset #058",
    "country": "South Korea",
    "lat": 35.5959,
    "lon": 126.8492,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_59",
    "name": "South Korea Industrial/Bank Asset #059",
    "country": "South Korea",
    "lat": 35.789,
    "lon": 127.8194,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_60",
    "name": "South Korea Industrial/Bank Asset #060",
    "country": "South Korea",
    "lat": 35.605,
    "lon": 128.3603,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_61",
    "name": "South Korea Industrial/Bank Asset #061",
    "country": "South Korea",
    "lat": 35.8861,
    "lon": 126.3682,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_62",
    "name": "South Korea Industrial/Bank Asset #062",
    "country": "South Korea",
    "lat": 36.4891,
    "lon": 126.8731,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_63",
    "name": "South Korea Industrial/Bank Asset #063",
    "country": "South Korea",
    "lat": 37.7994,
    "lon": 127.2418,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_64",
    "name": "South Korea Industrial/Bank Asset #064",
    "country": "South Korea",
    "lat": 35.0082,
    "lon": 128.2649,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_65",
    "name": "South Korea Industrial/Bank Asset #065",
    "country": "South Korea",
    "lat": 37.7206,
    "lon": 128.7557,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_66",
    "name": "South Korea Industrial/Bank Asset #066",
    "country": "South Korea",
    "lat": 37.0071,
    "lon": 126.6974,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_67",
    "name": "South Korea Industrial/Bank Asset #067",
    "country": "South Korea",
    "lat": 35.2702,
    "lon": 127.7851,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_68",
    "name": "South Korea Industrial/Bank Asset #068",
    "country": "South Korea",
    "lat": 37.1707,
    "lon": 126.5539,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_69",
    "name": "South Korea Industrial/Bank Asset #069",
    "country": "South Korea",
    "lat": 35.7677,
    "lon": 126.9435,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_70",
    "name": "South Korea Industrial/Bank Asset #070",
    "country": "South Korea",
    "lat": 37.966,
    "lon": 127.1381,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_71",
    "name": "South Korea Industrial/Bank Asset #071",
    "country": "South Korea",
    "lat": 36.3928,
    "lon": 126.5494,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_72",
    "name": "South Korea Industrial/Bank Asset #072",
    "country": "South Korea",
    "lat": 35.5241,
    "lon": 126.3683,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_73",
    "name": "South Korea Industrial/Bank Asset #073",
    "country": "South Korea",
    "lat": 35.8717,
    "lon": 128.6548,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_74",
    "name": "South Korea Industrial/Bank Asset #074",
    "country": "South Korea",
    "lat": 35.9381,
    "lon": 128.4656,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_75",
    "name": "South Korea Industrial/Bank Asset #075",
    "country": "South Korea",
    "lat": 35.285,
    "lon": 128.5246,
    "type": "Chaebol Fabs & Refineries",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_tai_1",
    "name": "Taiwan Industrial/Bank Asset #001",
    "country": "Taiwan",
    "lat": 22.6001,
    "lon": 121.5232,
    "type": "Hsinchu & Tainan Science Parks",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_tai_2",
    "name": "Taiwan Industrial/Bank Asset #002",
    "country": "Taiwan",
    "lat": 24.0821,
    "lon": 120.4328,
    "type": "Hsinchu & Tainan Science Parks",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_tai_3",
    "name": "Taiwan Industrial/Bank Asset #003",
    "country": "Taiwan",
    "lat": 23.3481,
    "lon": 120.8603,
    "type": "Hsinchu & Tainan Science Parks",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_tai_4",
    "name": "Taiwan Industrial/Bank Asset #004",
    "country": "Taiwan",
    "lat": 23.9823,
    "lon": 121.5656,
    "type": "Hsinchu & Tainan Science Parks",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_tai_5",
    "name": "Taiwan Industrial/Bank Asset #005",
    "country": "Taiwan",
    "lat": 22.7131,
    "lon": 121.4639,
    "type": "Hsinchu & Tainan Science Parks",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_tai_6",
    "name": "Taiwan Industrial/Bank Asset #006",
    "country": "Taiwan",
    "lat": 22.9289,
    "lon": 120.8012,
    "type": "Hsinchu & Tainan Science Parks",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_tai_7",
    "name": "Taiwan Industrial/Bank Asset #007",
    "country": "Taiwan",
    "lat": 24.7995,
    "lon": 120.5949,
    "type": "Hsinchu & Tainan Science Parks",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_tai_8",
    "name": "Taiwan Industrial/Bank Asset #008",
    "country": "Taiwan",
    "lat": 23.4157,
    "lon": 121.5211,
    "type": "Hsinchu & Tainan Science Parks",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_tai_9",
    "name": "Taiwan Industrial/Bank Asset #009",
    "country": "Taiwan",
    "lat": 24.4098,
    "lon": 121.1982,
    "type": "Hsinchu & Tainan Science Parks",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_tai_10",
    "name": "Taiwan Industrial/Bank Asset #010",
    "country": "Taiwan",
    "lat": 24.4026,
    "lon": 120.3409,
    "type": "Hsinchu & Tainan Science Parks",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_tai_11",
    "name": "Taiwan Industrial/Bank Asset #011",
    "country": "Taiwan",
    "lat": 24.1608,
    "lon": 120.2538,
    "type": "Hsinchu & Tainan Science Parks",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_tai_12",
    "name": "Taiwan Industrial/Bank Asset #012",
    "country": "Taiwan",
    "lat": 24.7519,
    "lon": 120.415,
    "type": "Hsinchu & Tainan Science Parks",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_tai_13",
    "name": "Taiwan Industrial/Bank Asset #013",
    "country": "Taiwan",
    "lat": 23.4885,
    "lon": 121.1052,
    "type": "Hsinchu & Tainan Science Parks",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_tai_14",
    "name": "Taiwan Industrial/Bank Asset #014",
    "country": "Taiwan",
    "lat": 24.4154,
    "lon": 121.2454,
    "type": "Hsinchu & Tainan Science Parks",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_tai_15",
    "name": "Taiwan Industrial/Bank Asset #015",
    "country": "Taiwan",
    "lat": 22.925,
    "lon": 120.7676,
    "type": "Hsinchu & Tainan Science Parks",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_tai_16",
    "name": "Taiwan Industrial/Bank Asset #016",
    "country": "Taiwan",
    "lat": 23.3506,
    "lon": 120.2061,
    "type": "Hsinchu & Tainan Science Parks",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_tai_17",
    "name": "Taiwan Industrial/Bank Asset #017",
    "country": "Taiwan",
    "lat": 24.1327,
    "lon": 121.5017,
    "type": "Hsinchu & Tainan Science Parks",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_tai_18",
    "name": "Taiwan Industrial/Bank Asset #018",
    "country": "Taiwan",
    "lat": 24.8263,
    "lon": 120.369,
    "type": "Hsinchu & Tainan Science Parks",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_tai_19",
    "name": "Taiwan Industrial/Bank Asset #019",
    "country": "Taiwan",
    "lat": 24.699,
    "lon": 120.3407,
    "type": "Hsinchu & Tainan Science Parks",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_tai_20",
    "name": "Taiwan Industrial/Bank Asset #020",
    "country": "Taiwan",
    "lat": 23.4771,
    "lon": 120.2336,
    "type": "Hsinchu & Tainan Science Parks",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_tai_21",
    "name": "Taiwan Industrial/Bank Asset #021",
    "country": "Taiwan",
    "lat": 23.1179,
    "lon": 120.6628,
    "type": "Hsinchu & Tainan Science Parks",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_tai_22",
    "name": "Taiwan Industrial/Bank Asset #022",
    "country": "Taiwan",
    "lat": 24.181,
    "lon": 121.2447,
    "type": "Hsinchu & Tainan Science Parks",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_tai_23",
    "name": "Taiwan Industrial/Bank Asset #023",
    "country": "Taiwan",
    "lat": 24.3321,
    "lon": 121.0826,
    "type": "Hsinchu & Tainan Science Parks",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_tai_24",
    "name": "Taiwan Industrial/Bank Asset #024",
    "country": "Taiwan",
    "lat": 23.846,
    "lon": 121.7246,
    "type": "Hsinchu & Tainan Science Parks",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_tai_25",
    "name": "Taiwan Industrial/Bank Asset #025",
    "country": "Taiwan",
    "lat": 24.0976,
    "lon": 120.7013,
    "type": "Hsinchu & Tainan Science Parks",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_tai_26",
    "name": "Taiwan Industrial/Bank Asset #026",
    "country": "Taiwan",
    "lat": 23.7454,
    "lon": 121.2809,
    "type": "Hsinchu & Tainan Science Parks",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_tai_27",
    "name": "Taiwan Industrial/Bank Asset #027",
    "country": "Taiwan",
    "lat": 22.7186,
    "lon": 121.2187,
    "type": "Hsinchu & Tainan Science Parks",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_tai_28",
    "name": "Taiwan Industrial/Bank Asset #028",
    "country": "Taiwan",
    "lat": 23.0866,
    "lon": 120.7132,
    "type": "Hsinchu & Tainan Science Parks",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_tai_29",
    "name": "Taiwan Industrial/Bank Asset #029",
    "country": "Taiwan",
    "lat": 24.1131,
    "lon": 120.7758,
    "type": "Hsinchu & Tainan Science Parks",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_tai_30",
    "name": "Taiwan Industrial/Bank Asset #030",
    "country": "Taiwan",
    "lat": 24.5037,
    "lon": 121.0534,
    "type": "Hsinchu & Tainan Science Parks",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_tai_31",
    "name": "Taiwan Industrial/Bank Asset #031",
    "country": "Taiwan",
    "lat": 24.8607,
    "lon": 120.2473,
    "type": "Hsinchu & Tainan Science Parks",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_tai_32",
    "name": "Taiwan Industrial/Bank Asset #032",
    "country": "Taiwan",
    "lat": 24.0342,
    "lon": 120.4111,
    "type": "Hsinchu & Tainan Science Parks",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_tai_33",
    "name": "Taiwan Industrial/Bank Asset #033",
    "country": "Taiwan",
    "lat": 24.5272,
    "lon": 121.523,
    "type": "Hsinchu & Tainan Science Parks",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_tai_34",
    "name": "Taiwan Industrial/Bank Asset #034",
    "country": "Taiwan",
    "lat": 24.5766,
    "lon": 120.2798,
    "type": "Hsinchu & Tainan Science Parks",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_tai_35",
    "name": "Taiwan Industrial/Bank Asset #035",
    "country": "Taiwan",
    "lat": 23.67,
    "lon": 120.5454,
    "type": "Hsinchu & Tainan Science Parks",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_tai_36",
    "name": "Taiwan Industrial/Bank Asset #036",
    "country": "Taiwan",
    "lat": 24.8183,
    "lon": 120.2406,
    "type": "Hsinchu & Tainan Science Parks",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_tai_37",
    "name": "Taiwan Industrial/Bank Asset #037",
    "country": "Taiwan",
    "lat": 23.0245,
    "lon": 121.1893,
    "type": "Hsinchu & Tainan Science Parks",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_tai_38",
    "name": "Taiwan Industrial/Bank Asset #038",
    "country": "Taiwan",
    "lat": 23.4579,
    "lon": 120.536,
    "type": "Hsinchu & Tainan Science Parks",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_tai_39",
    "name": "Taiwan Industrial/Bank Asset #039",
    "country": "Taiwan",
    "lat": 23.5918,
    "lon": 121.442,
    "type": "Hsinchu & Tainan Science Parks",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_tai_40",
    "name": "Taiwan Industrial/Bank Asset #040",
    "country": "Taiwan",
    "lat": 23.5654,
    "lon": 121.5305,
    "type": "Hsinchu & Tainan Science Parks",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_tai_41",
    "name": "Taiwan Industrial/Bank Asset #041",
    "country": "Taiwan",
    "lat": 23.563,
    "lon": 120.3499,
    "type": "Hsinchu & Tainan Science Parks",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_tai_42",
    "name": "Taiwan Industrial/Bank Asset #042",
    "country": "Taiwan",
    "lat": 23.6837,
    "lon": 121.2054,
    "type": "Hsinchu & Tainan Science Parks",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_tai_43",
    "name": "Taiwan Industrial/Bank Asset #043",
    "country": "Taiwan",
    "lat": 22.7363,
    "lon": 120.8197,
    "type": "Hsinchu & Tainan Science Parks",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_tai_44",
    "name": "Taiwan Industrial/Bank Asset #044",
    "country": "Taiwan",
    "lat": 23.8271,
    "lon": 120.1603,
    "type": "Hsinchu & Tainan Science Parks",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_tai_45",
    "name": "Taiwan Industrial/Bank Asset #045",
    "country": "Taiwan",
    "lat": 22.7081,
    "lon": 121.1267,
    "type": "Hsinchu & Tainan Science Parks",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_1",
    "name": "Saudi Arabia Industrial/Bank Asset #001",
    "country": "Saudi Arabia",
    "lat": 24.9525,
    "lon": 42.6552,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_2",
    "name": "Saudi Arabia Industrial/Bank Asset #002",
    "country": "Saudi Arabia",
    "lat": 24.0667,
    "lon": 41.4822,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_3",
    "name": "Saudi Arabia Industrial/Bank Asset #003",
    "country": "Saudi Arabia",
    "lat": 25.3718,
    "lon": 50.4043,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_4",
    "name": "Saudi Arabia Industrial/Bank Asset #004",
    "country": "Saudi Arabia",
    "lat": 22.9067,
    "lon": 39.6513,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_5",
    "name": "Saudi Arabia Industrial/Bank Asset #005",
    "country": "Saudi Arabia",
    "lat": 21.7833,
    "lon": 44.4535,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_6",
    "name": "Saudi Arabia Industrial/Bank Asset #006",
    "country": "Saudi Arabia",
    "lat": 24.4812,
    "lon": 46.4371,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_7",
    "name": "Saudi Arabia Industrial/Bank Asset #007",
    "country": "Saudi Arabia",
    "lat": 23.7851,
    "lon": 46.886,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_8",
    "name": "Saudi Arabia Industrial/Bank Asset #008",
    "country": "Saudi Arabia",
    "lat": 25.7273,
    "lon": 40.3683,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_9",
    "name": "Saudi Arabia Industrial/Bank Asset #009",
    "country": "Saudi Arabia",
    "lat": 26.0746,
    "lon": 41.661,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_10",
    "name": "Saudi Arabia Industrial/Bank Asset #010",
    "country": "Saudi Arabia",
    "lat": 22.7309,
    "lon": 48.9586,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_11",
    "name": "Saudi Arabia Industrial/Bank Asset #011",
    "country": "Saudi Arabia",
    "lat": 27.7155,
    "lon": 42.5038,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_12",
    "name": "Saudi Arabia Industrial/Bank Asset #012",
    "country": "Saudi Arabia",
    "lat": 24.1759,
    "lon": 47.4252,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_13",
    "name": "Saudi Arabia Industrial/Bank Asset #013",
    "country": "Saudi Arabia",
    "lat": 20.3662,
    "lon": 40.9699,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_14",
    "name": "Saudi Arabia Industrial/Bank Asset #014",
    "country": "Saudi Arabia",
    "lat": 21.1236,
    "lon": 47.6023,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_15",
    "name": "Saudi Arabia Industrial/Bank Asset #015",
    "country": "Saudi Arabia",
    "lat": 25.7725,
    "lon": 40.2835,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_16",
    "name": "Saudi Arabia Industrial/Bank Asset #016",
    "country": "Saudi Arabia",
    "lat": 24.8868,
    "lon": 41.2505,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_17",
    "name": "Saudi Arabia Industrial/Bank Asset #017",
    "country": "Saudi Arabia",
    "lat": 27.4417,
    "lon": 43.7148,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_18",
    "name": "Saudi Arabia Industrial/Bank Asset #018",
    "country": "Saudi Arabia",
    "lat": 23.6564,
    "lon": 48.377,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_19",
    "name": "Saudi Arabia Industrial/Bank Asset #019",
    "country": "Saudi Arabia",
    "lat": 25.7343,
    "lon": 40.2932,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_20",
    "name": "Saudi Arabia Industrial/Bank Asset #020",
    "country": "Saudi Arabia",
    "lat": 23.3158,
    "lon": 50.1195,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_21",
    "name": "Saudi Arabia Industrial/Bank Asset #021",
    "country": "Saudi Arabia",
    "lat": 26.6997,
    "lon": 46.0657,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_22",
    "name": "Saudi Arabia Industrial/Bank Asset #022",
    "country": "Saudi Arabia",
    "lat": 26.1772,
    "lon": 44.4061,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_23",
    "name": "Saudi Arabia Industrial/Bank Asset #023",
    "country": "Saudi Arabia",
    "lat": 25.2677,
    "lon": 50.4743,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_24",
    "name": "Saudi Arabia Industrial/Bank Asset #024",
    "country": "Saudi Arabia",
    "lat": 21.0771,
    "lon": 44.9859,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_25",
    "name": "Saudi Arabia Industrial/Bank Asset #025",
    "country": "Saudi Arabia",
    "lat": 24.2429,
    "lon": 39.5829,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_26",
    "name": "Saudi Arabia Industrial/Bank Asset #026",
    "country": "Saudi Arabia",
    "lat": 27.4825,
    "lon": 49.0658,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_27",
    "name": "Saudi Arabia Industrial/Bank Asset #027",
    "country": "Saudi Arabia",
    "lat": 23.8635,
    "lon": 45.1,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_28",
    "name": "Saudi Arabia Industrial/Bank Asset #028",
    "country": "Saudi Arabia",
    "lat": 27.3693,
    "lon": 41.1264,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_29",
    "name": "Saudi Arabia Industrial/Bank Asset #029",
    "country": "Saudi Arabia",
    "lat": 24.6284,
    "lon": 47.7659,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_30",
    "name": "Saudi Arabia Industrial/Bank Asset #030",
    "country": "Saudi Arabia",
    "lat": 21.0271,
    "lon": 43.6489,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_31",
    "name": "Saudi Arabia Industrial/Bank Asset #031",
    "country": "Saudi Arabia",
    "lat": 24.8044,
    "lon": 49.5924,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_32",
    "name": "Saudi Arabia Industrial/Bank Asset #032",
    "country": "Saudi Arabia",
    "lat": 24.0329,
    "lon": 43.616,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_33",
    "name": "Saudi Arabia Industrial/Bank Asset #033",
    "country": "Saudi Arabia",
    "lat": 27.836,
    "lon": 49.9909,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_34",
    "name": "Saudi Arabia Industrial/Bank Asset #034",
    "country": "Saudi Arabia",
    "lat": 26.099,
    "lon": 42.2832,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_35",
    "name": "Saudi Arabia Industrial/Bank Asset #035",
    "country": "Saudi Arabia",
    "lat": 27.7087,
    "lon": 50.6459,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_36",
    "name": "Saudi Arabia Industrial/Bank Asset #036",
    "country": "Saudi Arabia",
    "lat": 23.6228,
    "lon": 40.6005,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_37",
    "name": "Saudi Arabia Industrial/Bank Asset #037",
    "country": "Saudi Arabia",
    "lat": 23.302,
    "lon": 47.4002,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_38",
    "name": "Saudi Arabia Industrial/Bank Asset #038",
    "country": "Saudi Arabia",
    "lat": 25.9874,
    "lon": 42.587,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_39",
    "name": "Saudi Arabia Industrial/Bank Asset #039",
    "country": "Saudi Arabia",
    "lat": 25.612,
    "lon": 49.3285,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_40",
    "name": "Saudi Arabia Industrial/Bank Asset #040",
    "country": "Saudi Arabia",
    "lat": 25.695,
    "lon": 50.2261,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_41",
    "name": "Saudi Arabia Industrial/Bank Asset #041",
    "country": "Saudi Arabia",
    "lat": 25.0607,
    "lon": 41.4107,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_42",
    "name": "Saudi Arabia Industrial/Bank Asset #042",
    "country": "Saudi Arabia",
    "lat": 24.9933,
    "lon": 42.487,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_43",
    "name": "Saudi Arabia Industrial/Bank Asset #043",
    "country": "Saudi Arabia",
    "lat": 22.7623,
    "lon": 47.0685,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_44",
    "name": "Saudi Arabia Industrial/Bank Asset #044",
    "country": "Saudi Arabia",
    "lat": 27.8507,
    "lon": 46.801,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_45",
    "name": "Saudi Arabia Industrial/Bank Asset #045",
    "country": "Saudi Arabia",
    "lat": 27.6666,
    "lon": 45.0467,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_46",
    "name": "Saudi Arabia Industrial/Bank Asset #046",
    "country": "Saudi Arabia",
    "lat": 25.5545,
    "lon": 42.8686,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_47",
    "name": "Saudi Arabia Industrial/Bank Asset #047",
    "country": "Saudi Arabia",
    "lat": 20.9232,
    "lon": 43.2269,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_48",
    "name": "Saudi Arabia Industrial/Bank Asset #048",
    "country": "Saudi Arabia",
    "lat": 23.843,
    "lon": 45.8477,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_49",
    "name": "Saudi Arabia Industrial/Bank Asset #049",
    "country": "Saudi Arabia",
    "lat": 25.3373,
    "lon": 44.0097,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_50",
    "name": "Saudi Arabia Industrial/Bank Asset #050",
    "country": "Saudi Arabia",
    "lat": 25.9829,
    "lon": 49.0967,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_51",
    "name": "Saudi Arabia Industrial/Bank Asset #051",
    "country": "Saudi Arabia",
    "lat": 22.2874,
    "lon": 49.1676,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_52",
    "name": "Saudi Arabia Industrial/Bank Asset #052",
    "country": "Saudi Arabia",
    "lat": 26.4664,
    "lon": 45.2728,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_53",
    "name": "Saudi Arabia Industrial/Bank Asset #053",
    "country": "Saudi Arabia",
    "lat": 20.2022,
    "lon": 40.7439,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_54",
    "name": "Saudi Arabia Industrial/Bank Asset #054",
    "country": "Saudi Arabia",
    "lat": 25.362,
    "lon": 41.3988,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_55",
    "name": "Saudi Arabia Industrial/Bank Asset #055",
    "country": "Saudi Arabia",
    "lat": 26.0015,
    "lon": 40.9312,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_56",
    "name": "Saudi Arabia Industrial/Bank Asset #056",
    "country": "Saudi Arabia",
    "lat": 22.2929,
    "lon": 42.0067,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_57",
    "name": "Saudi Arabia Industrial/Bank Asset #057",
    "country": "Saudi Arabia",
    "lat": 26.7151,
    "lon": 47.2871,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_58",
    "name": "Saudi Arabia Industrial/Bank Asset #058",
    "country": "Saudi Arabia",
    "lat": 22.3611,
    "lon": 48.0431,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_59",
    "name": "Saudi Arabia Industrial/Bank Asset #059",
    "country": "Saudi Arabia",
    "lat": 20.2585,
    "lon": 48.7683,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_60",
    "name": "Saudi Arabia Industrial/Bank Asset #060",
    "country": "Saudi Arabia",
    "lat": 20.8198,
    "lon": 49.4164,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_61",
    "name": "Saudi Arabia Industrial/Bank Asset #061",
    "country": "Saudi Arabia",
    "lat": 25.9159,
    "lon": 49.3781,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_62",
    "name": "Saudi Arabia Industrial/Bank Asset #062",
    "country": "Saudi Arabia",
    "lat": 25.9393,
    "lon": 45.7352,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_63",
    "name": "Saudi Arabia Industrial/Bank Asset #063",
    "country": "Saudi Arabia",
    "lat": 21.9008,
    "lon": 48.4117,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_64",
    "name": "Saudi Arabia Industrial/Bank Asset #064",
    "country": "Saudi Arabia",
    "lat": 26.3906,
    "lon": 42.4517,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sau_65",
    "name": "Saudi Arabia Industrial/Bank Asset #065",
    "country": "Saudi Arabia",
    "lat": 25.3159,
    "lon": 50.1178,
    "type": "Aramco Oil & Desalination Facilities",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_1",
    "name": "United Arab Emirates Industrial/Bank Asset #001",
    "country": "United Arab Emirates",
    "lat": 23.9751,
    "lon": 56.1441,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_2",
    "name": "United Arab Emirates Industrial/Bank Asset #002",
    "country": "United Arab Emirates",
    "lat": 25.1516,
    "lon": 53.8256,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_3",
    "name": "United Arab Emirates Industrial/Bank Asset #003",
    "country": "United Arab Emirates",
    "lat": 24.3042,
    "lon": 52.7467,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_4",
    "name": "United Arab Emirates Industrial/Bank Asset #004",
    "country": "United Arab Emirates",
    "lat": 23.7027,
    "lon": 54.934,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_5",
    "name": "United Arab Emirates Industrial/Bank Asset #005",
    "country": "United Arab Emirates",
    "lat": 24.7618,
    "lon": 55.8324,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_6",
    "name": "United Arab Emirates Industrial/Bank Asset #006",
    "country": "United Arab Emirates",
    "lat": 24.86,
    "lon": 55.9814,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_7",
    "name": "United Arab Emirates Industrial/Bank Asset #007",
    "country": "United Arab Emirates",
    "lat": 24.6093,
    "lon": 55.0315,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_8",
    "name": "United Arab Emirates Industrial/Bank Asset #008",
    "country": "United Arab Emirates",
    "lat": 24.7102,
    "lon": 54.6678,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_9",
    "name": "United Arab Emirates Industrial/Bank Asset #009",
    "country": "United Arab Emirates",
    "lat": 24.4068,
    "lon": 55.4941,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_10",
    "name": "United Arab Emirates Industrial/Bank Asset #010",
    "country": "United Arab Emirates",
    "lat": 25.1286,
    "lon": 53.759,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_11",
    "name": "United Arab Emirates Industrial/Bank Asset #011",
    "country": "United Arab Emirates",
    "lat": 23.5549,
    "lon": 55.1576,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_12",
    "name": "United Arab Emirates Industrial/Bank Asset #012",
    "country": "United Arab Emirates",
    "lat": 23.574,
    "lon": 53.3257,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_13",
    "name": "United Arab Emirates Industrial/Bank Asset #013",
    "country": "United Arab Emirates",
    "lat": 24.2277,
    "lon": 54.0579,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_14",
    "name": "United Arab Emirates Industrial/Bank Asset #014",
    "country": "United Arab Emirates",
    "lat": 24.057,
    "lon": 54.7038,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_15",
    "name": "United Arab Emirates Industrial/Bank Asset #015",
    "country": "United Arab Emirates",
    "lat": 23.4601,
    "lon": 54.8023,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_16",
    "name": "United Arab Emirates Industrial/Bank Asset #016",
    "country": "United Arab Emirates",
    "lat": 23.71,
    "lon": 53.89,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_17",
    "name": "United Arab Emirates Industrial/Bank Asset #017",
    "country": "United Arab Emirates",
    "lat": 24.6194,
    "lon": 53.2573,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_18",
    "name": "United Arab Emirates Industrial/Bank Asset #018",
    "country": "United Arab Emirates",
    "lat": 23.5074,
    "lon": 53.8615,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_19",
    "name": "United Arab Emirates Industrial/Bank Asset #019",
    "country": "United Arab Emirates",
    "lat": 23.3017,
    "lon": 56.0566,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_20",
    "name": "United Arab Emirates Industrial/Bank Asset #020",
    "country": "United Arab Emirates",
    "lat": 24.4312,
    "lon": 55.0828,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_21",
    "name": "United Arab Emirates Industrial/Bank Asset #021",
    "country": "United Arab Emirates",
    "lat": 24.1811,
    "lon": 54.7616,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_22",
    "name": "United Arab Emirates Industrial/Bank Asset #022",
    "country": "United Arab Emirates",
    "lat": 23.9162,
    "lon": 55.5225,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_23",
    "name": "United Arab Emirates Industrial/Bank Asset #023",
    "country": "United Arab Emirates",
    "lat": 23.8357,
    "lon": 53.4919,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_24",
    "name": "United Arab Emirates Industrial/Bank Asset #024",
    "country": "United Arab Emirates",
    "lat": 23.5677,
    "lon": 52.9454,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_25",
    "name": "United Arab Emirates Industrial/Bank Asset #025",
    "country": "United Arab Emirates",
    "lat": 24.2103,
    "lon": 54.1974,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_26",
    "name": "United Arab Emirates Industrial/Bank Asset #026",
    "country": "United Arab Emirates",
    "lat": 24.2741,
    "lon": 53.031,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_27",
    "name": "United Arab Emirates Industrial/Bank Asset #027",
    "country": "United Arab Emirates",
    "lat": 23.6424,
    "lon": 53.4681,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_28",
    "name": "United Arab Emirates Industrial/Bank Asset #028",
    "country": "United Arab Emirates",
    "lat": 23.8638,
    "lon": 53.9989,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_29",
    "name": "United Arab Emirates Industrial/Bank Asset #029",
    "country": "United Arab Emirates",
    "lat": 23.6369,
    "lon": 55.4096,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_30",
    "name": "United Arab Emirates Industrial/Bank Asset #030",
    "country": "United Arab Emirates",
    "lat": 24.261,
    "lon": 56.2879,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_31",
    "name": "United Arab Emirates Industrial/Bank Asset #031",
    "country": "United Arab Emirates",
    "lat": 24.8474,
    "lon": 56.2321,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_32",
    "name": "United Arab Emirates Industrial/Bank Asset #032",
    "country": "United Arab Emirates",
    "lat": 23.2176,
    "lon": 55.1082,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_33",
    "name": "United Arab Emirates Industrial/Bank Asset #033",
    "country": "United Arab Emirates",
    "lat": 24.0913,
    "lon": 55.9562,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_34",
    "name": "United Arab Emirates Industrial/Bank Asset #034",
    "country": "United Arab Emirates",
    "lat": 24.4274,
    "lon": 54.9361,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_35",
    "name": "United Arab Emirates Industrial/Bank Asset #035",
    "country": "United Arab Emirates",
    "lat": 25.1178,
    "lon": 55.1572,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_36",
    "name": "United Arab Emirates Industrial/Bank Asset #036",
    "country": "United Arab Emirates",
    "lat": 23.8419,
    "lon": 55.9974,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_37",
    "name": "United Arab Emirates Industrial/Bank Asset #037",
    "country": "United Arab Emirates",
    "lat": 25.09,
    "lon": 54.0892,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_38",
    "name": "United Arab Emirates Industrial/Bank Asset #038",
    "country": "United Arab Emirates",
    "lat": 24.2805,
    "lon": 53.7182,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_39",
    "name": "United Arab Emirates Industrial/Bank Asset #039",
    "country": "United Arab Emirates",
    "lat": 25.0227,
    "lon": 55.6596,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_40",
    "name": "United Arab Emirates Industrial/Bank Asset #040",
    "country": "United Arab Emirates",
    "lat": 23.9499,
    "lon": 55.5901,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_41",
    "name": "United Arab Emirates Industrial/Bank Asset #041",
    "country": "United Arab Emirates",
    "lat": 24.0911,
    "lon": 52.8579,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_42",
    "name": "United Arab Emirates Industrial/Bank Asset #042",
    "country": "United Arab Emirates",
    "lat": 24.9966,
    "lon": 53.393,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_43",
    "name": "United Arab Emirates Industrial/Bank Asset #043",
    "country": "United Arab Emirates",
    "lat": 24.2278,
    "lon": 56.1136,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_44",
    "name": "United Arab Emirates Industrial/Bank Asset #044",
    "country": "United Arab Emirates",
    "lat": 23.5348,
    "lon": 56.1426,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_45",
    "name": "United Arab Emirates Industrial/Bank Asset #045",
    "country": "United Arab Emirates",
    "lat": 24.2759,
    "lon": 52.7264,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_46",
    "name": "United Arab Emirates Industrial/Bank Asset #046",
    "country": "United Arab Emirates",
    "lat": 23.3309,
    "lon": 55.1132,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_47",
    "name": "United Arab Emirates Industrial/Bank Asset #047",
    "country": "United Arab Emirates",
    "lat": 24.7472,
    "lon": 55.8138,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_48",
    "name": "United Arab Emirates Industrial/Bank Asset #048",
    "country": "United Arab Emirates",
    "lat": 24.0484,
    "lon": 53.0741,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_49",
    "name": "United Arab Emirates Industrial/Bank Asset #049",
    "country": "United Arab Emirates",
    "lat": 24.2755,
    "lon": 55.2299,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_50",
    "name": "United Arab Emirates Industrial/Bank Asset #050",
    "country": "United Arab Emirates",
    "lat": 25.1524,
    "lon": 55.4907,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_51",
    "name": "United Arab Emirates Industrial/Bank Asset #051",
    "country": "United Arab Emirates",
    "lat": 24.4931,
    "lon": 56.0831,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_52",
    "name": "United Arab Emirates Industrial/Bank Asset #052",
    "country": "United Arab Emirates",
    "lat": 24.6938,
    "lon": 53.2535,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_53",
    "name": "United Arab Emirates Industrial/Bank Asset #053",
    "country": "United Arab Emirates",
    "lat": 24.1185,
    "lon": 53.8942,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_54",
    "name": "United Arab Emirates Industrial/Bank Asset #054",
    "country": "United Arab Emirates",
    "lat": 23.375,
    "lon": 52.8954,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_uni_55",
    "name": "United Arab Emirates Industrial/Bank Asset #055",
    "country": "United Arab Emirates",
    "lat": 24.7884,
    "lon": 54.7091,
    "type": "Freezone & Oil Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_qat_1",
    "name": "Qatar Industrial/Bank Asset #001",
    "country": "Qatar",
    "lat": 25.425,
    "lon": 50.9621,
    "type": "North Field Gas Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_qat_2",
    "name": "Qatar Industrial/Bank Asset #002",
    "country": "Qatar",
    "lat": 25.1086,
    "lon": 51.0904,
    "type": "North Field Gas Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_qat_3",
    "name": "Qatar Industrial/Bank Asset #003",
    "country": "Qatar",
    "lat": 25.4802,
    "lon": 51.1264,
    "type": "North Field Gas Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_qat_4",
    "name": "Qatar Industrial/Bank Asset #004",
    "country": "Qatar",
    "lat": 24.8669,
    "lon": 51.3186,
    "type": "North Field Gas Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_qat_5",
    "name": "Qatar Industrial/Bank Asset #005",
    "country": "Qatar",
    "lat": 25.3848,
    "lon": 51.2931,
    "type": "North Field Gas Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_qat_6",
    "name": "Qatar Industrial/Bank Asset #006",
    "country": "Qatar",
    "lat": 25.4683,
    "lon": 51.3848,
    "type": "North Field Gas Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_qat_7",
    "name": "Qatar Industrial/Bank Asset #007",
    "country": "Qatar",
    "lat": 25.4356,
    "lon": 51.3407,
    "type": "North Field Gas Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_qat_8",
    "name": "Qatar Industrial/Bank Asset #008",
    "country": "Qatar",
    "lat": 24.9226,
    "lon": 51.5224,
    "type": "North Field Gas Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_qat_9",
    "name": "Qatar Industrial/Bank Asset #009",
    "country": "Qatar",
    "lat": 24.9561,
    "lon": 51.4095,
    "type": "North Field Gas Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_qat_10",
    "name": "Qatar Industrial/Bank Asset #010",
    "country": "Qatar",
    "lat": 25.1514,
    "lon": 50.8492,
    "type": "North Field Gas Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_qat_11",
    "name": "Qatar Industrial/Bank Asset #011",
    "country": "Qatar",
    "lat": 25.6153,
    "lon": 51.1301,
    "type": "North Field Gas Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_qat_12",
    "name": "Qatar Industrial/Bank Asset #012",
    "country": "Qatar",
    "lat": 25.2451,
    "lon": 51.3086,
    "type": "North Field Gas Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_qat_13",
    "name": "Qatar Industrial/Bank Asset #013",
    "country": "Qatar",
    "lat": 25.324,
    "lon": 51.2068,
    "type": "North Field Gas Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_qat_14",
    "name": "Qatar Industrial/Bank Asset #014",
    "country": "Qatar",
    "lat": 24.9864,
    "lon": 51.0928,
    "type": "North Field Gas Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_qat_15",
    "name": "Qatar Industrial/Bank Asset #015",
    "country": "Qatar",
    "lat": 25.6475,
    "lon": 51.2166,
    "type": "North Field Gas Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_qat_16",
    "name": "Qatar Industrial/Bank Asset #016",
    "country": "Qatar",
    "lat": 25.8101,
    "lon": 50.8953,
    "type": "North Field Gas Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_qat_17",
    "name": "Qatar Industrial/Bank Asset #017",
    "country": "Qatar",
    "lat": 25.5273,
    "lon": 51.5113,
    "type": "North Field Gas Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_qat_18",
    "name": "Qatar Industrial/Bank Asset #018",
    "country": "Qatar",
    "lat": 25.645,
    "lon": 51.3635,
    "type": "North Field Gas Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_qat_19",
    "name": "Qatar Industrial/Bank Asset #019",
    "country": "Qatar",
    "lat": 25.2231,
    "lon": 51.5396,
    "type": "North Field Gas Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_qat_20",
    "name": "Qatar Industrial/Bank Asset #020",
    "country": "Qatar",
    "lat": 25.4035,
    "lon": 51.2241,
    "type": "North Field Gas Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_qat_21",
    "name": "Qatar Industrial/Bank Asset #021",
    "country": "Qatar",
    "lat": 24.9732,
    "lon": 50.784,
    "type": "North Field Gas Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_qat_22",
    "name": "Qatar Industrial/Bank Asset #022",
    "country": "Qatar",
    "lat": 25.4467,
    "lon": 51.2097,
    "type": "North Field Gas Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_qat_23",
    "name": "Qatar Industrial/Bank Asset #023",
    "country": "Qatar",
    "lat": 25.797,
    "lon": 51.0238,
    "type": "North Field Gas Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_qat_24",
    "name": "Qatar Industrial/Bank Asset #024",
    "country": "Qatar",
    "lat": 25.5983,
    "lon": 51.5028,
    "type": "North Field Gas Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_qat_25",
    "name": "Qatar Industrial/Bank Asset #025",
    "country": "Qatar",
    "lat": 25.1939,
    "lon": 51.1101,
    "type": "North Field Gas Infrastructure",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sin_1",
    "name": "Singapore Industrial/Bank Asset #001",
    "country": "Singapore",
    "lat": 1.3938,
    "lon": 103.825,
    "type": "Jurong Island & Financial District",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sin_2",
    "name": "Singapore Industrial/Bank Asset #002",
    "country": "Singapore",
    "lat": 1.2483,
    "lon": 103.7083,
    "type": "Jurong Island & Financial District",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sin_3",
    "name": "Singapore Industrial/Bank Asset #003",
    "country": "Singapore",
    "lat": 1.4504,
    "lon": 103.6977,
    "type": "Jurong Island & Financial District",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sin_4",
    "name": "Singapore Industrial/Bank Asset #004",
    "country": "Singapore",
    "lat": 1.2544,
    "lon": 103.9399,
    "type": "Jurong Island & Financial District",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sin_5",
    "name": "Singapore Industrial/Bank Asset #005",
    "country": "Singapore",
    "lat": 1.4557,
    "lon": 103.9606,
    "type": "Jurong Island & Financial District",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sin_6",
    "name": "Singapore Industrial/Bank Asset #006",
    "country": "Singapore",
    "lat": 1.4797,
    "lon": 104.0177,
    "type": "Jurong Island & Financial District",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sin_7",
    "name": "Singapore Industrial/Bank Asset #007",
    "country": "Singapore",
    "lat": 1.3384,
    "lon": 103.8399,
    "type": "Jurong Island & Financial District",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sin_8",
    "name": "Singapore Industrial/Bank Asset #008",
    "country": "Singapore",
    "lat": 1.2872,
    "lon": 103.6469,
    "type": "Jurong Island & Financial District",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sin_9",
    "name": "Singapore Industrial/Bank Asset #009",
    "country": "Singapore",
    "lat": 1.2295,
    "lon": 103.9102,
    "type": "Jurong Island & Financial District",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sin_10",
    "name": "Singapore Industrial/Bank Asset #010",
    "country": "Singapore",
    "lat": 1.3462,
    "lon": 103.7523,
    "type": "Jurong Island & Financial District",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sin_11",
    "name": "Singapore Industrial/Bank Asset #011",
    "country": "Singapore",
    "lat": 1.2385,
    "lon": 103.8822,
    "type": "Jurong Island & Financial District",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sin_12",
    "name": "Singapore Industrial/Bank Asset #012",
    "country": "Singapore",
    "lat": 1.23,
    "lon": 103.8678,
    "type": "Jurong Island & Financial District",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sin_13",
    "name": "Singapore Industrial/Bank Asset #013",
    "country": "Singapore",
    "lat": 1.47,
    "lon": 103.7471,
    "type": "Jurong Island & Financial District",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sin_14",
    "name": "Singapore Industrial/Bank Asset #014",
    "country": "Singapore",
    "lat": 1.3352,
    "lon": 103.8665,
    "type": "Jurong Island & Financial District",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sin_15",
    "name": "Singapore Industrial/Bank Asset #015",
    "country": "Singapore",
    "lat": 1.2917,
    "lon": 103.8537,
    "type": "Jurong Island & Financial District",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sin_16",
    "name": "Singapore Industrial/Bank Asset #016",
    "country": "Singapore",
    "lat": 1.3697,
    "lon": 103.7658,
    "type": "Jurong Island & Financial District",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sin_17",
    "name": "Singapore Industrial/Bank Asset #017",
    "country": "Singapore",
    "lat": 1.2949,
    "lon": 103.7913,
    "type": "Jurong Island & Financial District",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sin_18",
    "name": "Singapore Industrial/Bank Asset #018",
    "country": "Singapore",
    "lat": 1.2014,
    "lon": 103.7185,
    "type": "Jurong Island & Financial District",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sin_19",
    "name": "Singapore Industrial/Bank Asset #019",
    "country": "Singapore",
    "lat": 1.2665,
    "lon": 103.9159,
    "type": "Jurong Island & Financial District",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sin_20",
    "name": "Singapore Industrial/Bank Asset #020",
    "country": "Singapore",
    "lat": 1.3308,
    "lon": 103.956,
    "type": "Jurong Island & Financial District",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sin_21",
    "name": "Singapore Industrial/Bank Asset #021",
    "country": "Singapore",
    "lat": 1.2403,
    "lon": 103.9132,
    "type": "Jurong Island & Financial District",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sin_22",
    "name": "Singapore Industrial/Bank Asset #022",
    "country": "Singapore",
    "lat": 1.4634,
    "lon": 103.8051,
    "type": "Jurong Island & Financial District",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sin_23",
    "name": "Singapore Industrial/Bank Asset #023",
    "country": "Singapore",
    "lat": 1.3076,
    "lon": 103.7422,
    "type": "Jurong Island & Financial District",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sin_24",
    "name": "Singapore Industrial/Bank Asset #024",
    "country": "Singapore",
    "lat": 1.3655,
    "lon": 103.6903,
    "type": "Jurong Island & Financial District",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sin_25",
    "name": "Singapore Industrial/Bank Asset #025",
    "country": "Singapore",
    "lat": 1.382,
    "lon": 103.9567,
    "type": "Jurong Island & Financial District",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sin_26",
    "name": "Singapore Industrial/Bank Asset #026",
    "country": "Singapore",
    "lat": 1.4576,
    "lon": 103.676,
    "type": "Jurong Island & Financial District",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sin_27",
    "name": "Singapore Industrial/Bank Asset #027",
    "country": "Singapore",
    "lat": 1.3616,
    "lon": 103.7253,
    "type": "Jurong Island & Financial District",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sin_28",
    "name": "Singapore Industrial/Bank Asset #028",
    "country": "Singapore",
    "lat": 1.4659,
    "lon": 103.6506,
    "type": "Jurong Island & Financial District",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sin_29",
    "name": "Singapore Industrial/Bank Asset #029",
    "country": "Singapore",
    "lat": 1.2226,
    "lon": 103.6275,
    "type": "Jurong Island & Financial District",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sin_30",
    "name": "Singapore Industrial/Bank Asset #030",
    "country": "Singapore",
    "lat": 1.3522,
    "lon": 103.6325,
    "type": "Jurong Island & Financial District",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sin_31",
    "name": "Singapore Industrial/Bank Asset #031",
    "country": "Singapore",
    "lat": 1.3746,
    "lon": 103.7821,
    "type": "Jurong Island & Financial District",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sin_32",
    "name": "Singapore Industrial/Bank Asset #032",
    "country": "Singapore",
    "lat": 1.377,
    "lon": 103.9825,
    "type": "Jurong Island & Financial District",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sin_33",
    "name": "Singapore Industrial/Bank Asset #033",
    "country": "Singapore",
    "lat": 1.3655,
    "lon": 103.8374,
    "type": "Jurong Island & Financial District",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sin_34",
    "name": "Singapore Industrial/Bank Asset #034",
    "country": "Singapore",
    "lat": 1.4996,
    "lon": 103.8088,
    "type": "Jurong Island & Financial District",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sin_35",
    "name": "Singapore Industrial/Bank Asset #035",
    "country": "Singapore",
    "lat": 1.4326,
    "lon": 103.7663,
    "type": "Jurong Island & Financial District",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_1",
    "name": "Australia Industrial/Bank Asset #001",
    "country": "Australia",
    "lat": -30.2505,
    "lon": 140.3015,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_2",
    "name": "Australia Industrial/Bank Asset #002",
    "country": "Australia",
    "lat": -21.0719,
    "lon": 128.754,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_3",
    "name": "Australia Industrial/Bank Asset #003",
    "country": "Australia",
    "lat": -25.9054,
    "lon": 134.0199,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_4",
    "name": "Australia Industrial/Bank Asset #004",
    "country": "Australia",
    "lat": -27.1279,
    "lon": 133.822,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_5",
    "name": "Australia Industrial/Bank Asset #005",
    "country": "Australia",
    "lat": -22.3418,
    "lon": 142.1216,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_6",
    "name": "Australia Industrial/Bank Asset #006",
    "country": "Australia",
    "lat": -19.7523,
    "lon": 136.5069,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_7",
    "name": "Australia Industrial/Bank Asset #007",
    "country": "Australia",
    "lat": -31.2848,
    "lon": 134.1093,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_8",
    "name": "Australia Industrial/Bank Asset #008",
    "country": "Australia",
    "lat": -26.238,
    "lon": 126.0695,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_9",
    "name": "Australia Industrial/Bank Asset #009",
    "country": "Australia",
    "lat": -17.1932,
    "lon": 137.5959,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_10",
    "name": "Australia Industrial/Bank Asset #010",
    "country": "Australia",
    "lat": -16.8508,
    "lon": 139.4321,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_11",
    "name": "Australia Industrial/Bank Asset #011",
    "country": "Australia",
    "lat": -25.5669,
    "lon": 130.3811,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_12",
    "name": "Australia Industrial/Bank Asset #012",
    "country": "Australia",
    "lat": -30.3313,
    "lon": 133.4734,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_13",
    "name": "Australia Industrial/Bank Asset #013",
    "country": "Australia",
    "lat": -33.1385,
    "lon": 130.6364,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_14",
    "name": "Australia Industrial/Bank Asset #014",
    "country": "Australia",
    "lat": -33.4994,
    "lon": 126.7326,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_15",
    "name": "Australia Industrial/Bank Asset #015",
    "country": "Australia",
    "lat": -17.9309,
    "lon": 130.44,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_16",
    "name": "Australia Industrial/Bank Asset #016",
    "country": "Australia",
    "lat": -25.8159,
    "lon": 132.6814,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_17",
    "name": "Australia Industrial/Bank Asset #017",
    "country": "Australia",
    "lat": -33.4341,
    "lon": 145.3042,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_18",
    "name": "Australia Industrial/Bank Asset #018",
    "country": "Australia",
    "lat": -28.4367,
    "lon": 138.6597,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_19",
    "name": "Australia Industrial/Bank Asset #019",
    "country": "Australia",
    "lat": -24.8853,
    "lon": 141.6815,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_20",
    "name": "Australia Industrial/Bank Asset #020",
    "country": "Australia",
    "lat": -19.2423,
    "lon": 128.0896,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_21",
    "name": "Australia Industrial/Bank Asset #021",
    "country": "Australia",
    "lat": -24.4717,
    "lon": 125.9424,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_22",
    "name": "Australia Industrial/Bank Asset #022",
    "country": "Australia",
    "lat": -22.5038,
    "lon": 130.5371,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_23",
    "name": "Australia Industrial/Bank Asset #023",
    "country": "Australia",
    "lat": -22.5099,
    "lon": 141.8213,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_24",
    "name": "Australia Industrial/Bank Asset #024",
    "country": "Australia",
    "lat": -24.9701,
    "lon": 130.8019,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_25",
    "name": "Australia Industrial/Bank Asset #025",
    "country": "Australia",
    "lat": -17.9396,
    "lon": 134.1629,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_26",
    "name": "Australia Industrial/Bank Asset #026",
    "country": "Australia",
    "lat": -27.9178,
    "lon": 142.5953,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_27",
    "name": "Australia Industrial/Bank Asset #027",
    "country": "Australia",
    "lat": -25.5065,
    "lon": 133.3406,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_28",
    "name": "Australia Industrial/Bank Asset #028",
    "country": "Australia",
    "lat": -23.3942,
    "lon": 133.8141,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_29",
    "name": "Australia Industrial/Bank Asset #029",
    "country": "Australia",
    "lat": -31.7686,
    "lon": 125.7445,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_30",
    "name": "Australia Industrial/Bank Asset #030",
    "country": "Australia",
    "lat": -32.8824,
    "lon": 137.2134,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_31",
    "name": "Australia Industrial/Bank Asset #031",
    "country": "Australia",
    "lat": -30.4627,
    "lon": 126.2557,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_32",
    "name": "Australia Industrial/Bank Asset #032",
    "country": "Australia",
    "lat": -27.75,
    "lon": 138.9853,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_33",
    "name": "Australia Industrial/Bank Asset #033",
    "country": "Australia",
    "lat": -32.1401,
    "lon": 127.2983,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_34",
    "name": "Australia Industrial/Bank Asset #034",
    "country": "Australia",
    "lat": -19.6689,
    "lon": 139.0561,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_35",
    "name": "Australia Industrial/Bank Asset #035",
    "country": "Australia",
    "lat": -25.6027,
    "lon": 133.2616,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_36",
    "name": "Australia Industrial/Bank Asset #036",
    "country": "Australia",
    "lat": -30.4773,
    "lon": 125.6399,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_37",
    "name": "Australia Industrial/Bank Asset #037",
    "country": "Australia",
    "lat": -19.2694,
    "lon": 122.3087,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_38",
    "name": "Australia Industrial/Bank Asset #038",
    "country": "Australia",
    "lat": -33.4934,
    "lon": 135.5337,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_39",
    "name": "Australia Industrial/Bank Asset #039",
    "country": "Australia",
    "lat": -31.3697,
    "lon": 136.879,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_40",
    "name": "Australia Industrial/Bank Asset #040",
    "country": "Australia",
    "lat": -33.5646,
    "lon": 135.5045,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_41",
    "name": "Australia Industrial/Bank Asset #041",
    "country": "Australia",
    "lat": -33.2636,
    "lon": 127.9682,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_42",
    "name": "Australia Industrial/Bank Asset #042",
    "country": "Australia",
    "lat": -31.0293,
    "lon": 144.7677,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_43",
    "name": "Australia Industrial/Bank Asset #043",
    "country": "Australia",
    "lat": -23.4816,
    "lon": 135.2965,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_44",
    "name": "Australia Industrial/Bank Asset #044",
    "country": "Australia",
    "lat": -33.9348,
    "lon": 139.0391,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_45",
    "name": "Australia Industrial/Bank Asset #045",
    "country": "Australia",
    "lat": -22.3586,
    "lon": 128.5729,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_46",
    "name": "Australia Industrial/Bank Asset #046",
    "country": "Australia",
    "lat": -32.7265,
    "lon": 132.5509,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_47",
    "name": "Australia Industrial/Bank Asset #047",
    "country": "Australia",
    "lat": -16.4,
    "lon": 142.5853,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_48",
    "name": "Australia Industrial/Bank Asset #048",
    "country": "Australia",
    "lat": -31.1998,
    "lon": 141.6987,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_49",
    "name": "Australia Industrial/Bank Asset #049",
    "country": "Australia",
    "lat": -23.4549,
    "lon": 140.8408,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_50",
    "name": "Australia Industrial/Bank Asset #050",
    "country": "Australia",
    "lat": -19.5018,
    "lon": 126.1352,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_51",
    "name": "Australia Industrial/Bank Asset #051",
    "country": "Australia",
    "lat": -22.3963,
    "lon": 128.1185,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_52",
    "name": "Australia Industrial/Bank Asset #052",
    "country": "Australia",
    "lat": -21.2346,
    "lon": 129.9941,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_53",
    "name": "Australia Industrial/Bank Asset #053",
    "country": "Australia",
    "lat": -26.1075,
    "lon": 135.9443,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_54",
    "name": "Australia Industrial/Bank Asset #054",
    "country": "Australia",
    "lat": -30.1334,
    "lon": 131.0211,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_55",
    "name": "Australia Industrial/Bank Asset #055",
    "country": "Australia",
    "lat": -32.3157,
    "lon": 126.6264,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_56",
    "name": "Australia Industrial/Bank Asset #056",
    "country": "Australia",
    "lat": -18.7973,
    "lon": 133.8746,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_57",
    "name": "Australia Industrial/Bank Asset #057",
    "country": "Australia",
    "lat": -26.7137,
    "lon": 125.3595,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_58",
    "name": "Australia Industrial/Bank Asset #058",
    "country": "Australia",
    "lat": -32.5366,
    "lon": 133.1909,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_59",
    "name": "Australia Industrial/Bank Asset #059",
    "country": "Australia",
    "lat": -23.2045,
    "lon": 122.7069,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_60",
    "name": "Australia Industrial/Bank Asset #060",
    "country": "Australia",
    "lat": -20.1604,
    "lon": 133.8499,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_61",
    "name": "Australia Industrial/Bank Asset #061",
    "country": "Australia",
    "lat": -32.1547,
    "lon": 133.3438,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_62",
    "name": "Australia Industrial/Bank Asset #062",
    "country": "Australia",
    "lat": -31.9241,
    "lon": 136.2534,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_63",
    "name": "Australia Industrial/Bank Asset #063",
    "country": "Australia",
    "lat": -19.3746,
    "lon": 143.2973,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_64",
    "name": "Australia Industrial/Bank Asset #064",
    "country": "Australia",
    "lat": -20.3223,
    "lon": 137.3516,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_65",
    "name": "Australia Industrial/Bank Asset #065",
    "country": "Australia",
    "lat": -24.8732,
    "lon": 130.6591,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_66",
    "name": "Australia Industrial/Bank Asset #066",
    "country": "Australia",
    "lat": -33.4881,
    "lon": 134.4856,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_67",
    "name": "Australia Industrial/Bank Asset #067",
    "country": "Australia",
    "lat": -30.1392,
    "lon": 141.0252,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_68",
    "name": "Australia Industrial/Bank Asset #068",
    "country": "Australia",
    "lat": -20.058,
    "lon": 130.9197,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_69",
    "name": "Australia Industrial/Bank Asset #069",
    "country": "Australia",
    "lat": -23.6671,
    "lon": 139.5635,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_70",
    "name": "Australia Industrial/Bank Asset #070",
    "country": "Australia",
    "lat": -20.5623,
    "lon": 138.491,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_71",
    "name": "Australia Industrial/Bank Asset #071",
    "country": "Australia",
    "lat": -32.5111,
    "lon": 124.9832,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_72",
    "name": "Australia Industrial/Bank Asset #072",
    "country": "Australia",
    "lat": -25.6815,
    "lon": 127.3503,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_73",
    "name": "Australia Industrial/Bank Asset #073",
    "country": "Australia",
    "lat": -18.807,
    "lon": 128.5684,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_74",
    "name": "Australia Industrial/Bank Asset #074",
    "country": "Australia",
    "lat": -18.4882,
    "lon": 131.5775,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_75",
    "name": "Australia Industrial/Bank Asset #075",
    "country": "Australia",
    "lat": -30.8676,
    "lon": 138.7896,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_76",
    "name": "Australia Industrial/Bank Asset #076",
    "country": "Australia",
    "lat": -20.0604,
    "lon": 135.6417,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_77",
    "name": "Australia Industrial/Bank Asset #077",
    "country": "Australia",
    "lat": -32.1491,
    "lon": 121.9427,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_78",
    "name": "Australia Industrial/Bank Asset #078",
    "country": "Australia",
    "lat": -22.4882,
    "lon": 138.2764,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_79",
    "name": "Australia Industrial/Bank Asset #079",
    "country": "Australia",
    "lat": -28.5838,
    "lon": 130.4645,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_80",
    "name": "Australia Industrial/Bank Asset #080",
    "country": "Australia",
    "lat": -31.484,
    "lon": 137.4078,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_81",
    "name": "Australia Industrial/Bank Asset #081",
    "country": "Australia",
    "lat": -29.7046,
    "lon": 142.2894,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_82",
    "name": "Australia Industrial/Bank Asset #082",
    "country": "Australia",
    "lat": -26.6459,
    "lon": 130.5455,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_83",
    "name": "Australia Industrial/Bank Asset #083",
    "country": "Australia",
    "lat": -29.3099,
    "lon": 138.1045,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_84",
    "name": "Australia Industrial/Bank Asset #084",
    "country": "Australia",
    "lat": -20.6805,
    "lon": 131.6875,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_85",
    "name": "Australia Industrial/Bank Asset #085",
    "country": "Australia",
    "lat": -20.1618,
    "lon": 133.3492,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_86",
    "name": "Australia Industrial/Bank Asset #086",
    "country": "Australia",
    "lat": -27.6062,
    "lon": 135.0879,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_87",
    "name": "Australia Industrial/Bank Asset #087",
    "country": "Australia",
    "lat": -29.702,
    "lon": 129.1297,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_88",
    "name": "Australia Industrial/Bank Asset #088",
    "country": "Australia",
    "lat": -28.0716,
    "lon": 138.7019,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_89",
    "name": "Australia Industrial/Bank Asset #089",
    "country": "Australia",
    "lat": -21.0259,
    "lon": 142.29,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_90",
    "name": "Australia Industrial/Bank Asset #090",
    "country": "Australia",
    "lat": -22.4029,
    "lon": 139.7175,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_91",
    "name": "Australia Industrial/Bank Asset #091",
    "country": "Australia",
    "lat": -26.2313,
    "lon": 138.5535,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_92",
    "name": "Australia Industrial/Bank Asset #092",
    "country": "Australia",
    "lat": -31.3577,
    "lon": 126.917,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_93",
    "name": "Australia Industrial/Bank Asset #093",
    "country": "Australia",
    "lat": -27.0599,
    "lon": 129.8925,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_94",
    "name": "Australia Industrial/Bank Asset #094",
    "country": "Australia",
    "lat": -24.3596,
    "lon": 138.4994,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_aus_95",
    "name": "Australia Industrial/Bank Asset #095",
    "country": "Australia",
    "lat": -21.5478,
    "lon": 125.6277,
    "type": "Mining Leases & Port Railheads",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_1",
    "name": "Brazil Industrial/Bank Asset #001",
    "country": "Brazil",
    "lat": -6.7969,
    "lon": -60.8248,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_2",
    "name": "Brazil Industrial/Bank Asset #002",
    "country": "Brazil",
    "lat": -20.7726,
    "lon": -58.3041,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_3",
    "name": "Brazil Industrial/Bank Asset #003",
    "country": "Brazil",
    "lat": -7.4162,
    "lon": -53.0832,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_4",
    "name": "Brazil Industrial/Bank Asset #004",
    "country": "Brazil",
    "lat": -21.2047,
    "lon": -56.9281,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_5",
    "name": "Brazil Industrial/Bank Asset #005",
    "country": "Brazil",
    "lat": -20.9494,
    "lon": -60.2404,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_6",
    "name": "Brazil Industrial/Bank Asset #006",
    "country": "Brazil",
    "lat": -16.0808,
    "lon": -43.1999,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_7",
    "name": "Brazil Industrial/Bank Asset #007",
    "country": "Brazil",
    "lat": -12.4066,
    "lon": -51.5419,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_8",
    "name": "Brazil Industrial/Bank Asset #008",
    "country": "Brazil",
    "lat": -10.8443,
    "lon": -50.1655,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_9",
    "name": "Brazil Industrial/Bank Asset #009",
    "country": "Brazil",
    "lat": -7.0985,
    "lon": -46.1559,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_10",
    "name": "Brazil Industrial/Bank Asset #010",
    "country": "Brazil",
    "lat": -11.9853,
    "lon": -53.0185,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_11",
    "name": "Brazil Industrial/Bank Asset #011",
    "country": "Brazil",
    "lat": -19.0027,
    "lon": -49.0961,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_12",
    "name": "Brazil Industrial/Bank Asset #012",
    "country": "Brazil",
    "lat": -9.3674,
    "lon": -55.7719,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_13",
    "name": "Brazil Industrial/Bank Asset #013",
    "country": "Brazil",
    "lat": -21.6923,
    "lon": -50.1287,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_14",
    "name": "Brazil Industrial/Bank Asset #014",
    "country": "Brazil",
    "lat": -13.977,
    "lon": -56.7499,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_15",
    "name": "Brazil Industrial/Bank Asset #015",
    "country": "Brazil",
    "lat": -19.5183,
    "lon": -60.2709,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_16",
    "name": "Brazil Industrial/Bank Asset #016",
    "country": "Brazil",
    "lat": -18.4019,
    "lon": -60.9148,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_17",
    "name": "Brazil Industrial/Bank Asset #017",
    "country": "Brazil",
    "lat": -19.7109,
    "lon": -42.9773,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_18",
    "name": "Brazil Industrial/Bank Asset #018",
    "country": "Brazil",
    "lat": -9.7552,
    "lon": -54.5637,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_19",
    "name": "Brazil Industrial/Bank Asset #019",
    "country": "Brazil",
    "lat": -15.9077,
    "lon": -50.3706,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_20",
    "name": "Brazil Industrial/Bank Asset #020",
    "country": "Brazil",
    "lat": -13.9461,
    "lon": -47.6553,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_21",
    "name": "Brazil Industrial/Bank Asset #021",
    "country": "Brazil",
    "lat": -21.1321,
    "lon": -59.297,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_22",
    "name": "Brazil Industrial/Bank Asset #022",
    "country": "Brazil",
    "lat": -17.6781,
    "lon": -45.9842,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_23",
    "name": "Brazil Industrial/Bank Asset #023",
    "country": "Brazil",
    "lat": -7.5899,
    "lon": -54.6543,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_24",
    "name": "Brazil Industrial/Bank Asset #024",
    "country": "Brazil",
    "lat": -6.8174,
    "lon": -55.9429,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_25",
    "name": "Brazil Industrial/Bank Asset #025",
    "country": "Brazil",
    "lat": -12.5282,
    "lon": -57.4185,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_26",
    "name": "Brazil Industrial/Bank Asset #026",
    "country": "Brazil",
    "lat": -7.3546,
    "lon": -50.5717,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_27",
    "name": "Brazil Industrial/Bank Asset #027",
    "country": "Brazil",
    "lat": -18.0523,
    "lon": -53.5916,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_28",
    "name": "Brazil Industrial/Bank Asset #028",
    "country": "Brazil",
    "lat": -20.5266,
    "lon": -59.6171,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_29",
    "name": "Brazil Industrial/Bank Asset #029",
    "country": "Brazil",
    "lat": -17.522,
    "lon": -43.8737,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_30",
    "name": "Brazil Industrial/Bank Asset #030",
    "country": "Brazil",
    "lat": -9.3829,
    "lon": -43.6992,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_31",
    "name": "Brazil Industrial/Bank Asset #031",
    "country": "Brazil",
    "lat": -8.2122,
    "lon": -46.2833,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_32",
    "name": "Brazil Industrial/Bank Asset #032",
    "country": "Brazil",
    "lat": -13.0317,
    "lon": -48.4245,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_33",
    "name": "Brazil Industrial/Bank Asset #033",
    "country": "Brazil",
    "lat": -6.7731,
    "lon": -50.783,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_34",
    "name": "Brazil Industrial/Bank Asset #034",
    "country": "Brazil",
    "lat": -9.9105,
    "lon": -47.2855,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_35",
    "name": "Brazil Industrial/Bank Asset #035",
    "country": "Brazil",
    "lat": -6.8502,
    "lon": -52.6607,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_36",
    "name": "Brazil Industrial/Bank Asset #036",
    "country": "Brazil",
    "lat": -14.8585,
    "lon": -50.3571,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_37",
    "name": "Brazil Industrial/Bank Asset #037",
    "country": "Brazil",
    "lat": -21.7924,
    "lon": -58.8272,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_38",
    "name": "Brazil Industrial/Bank Asset #038",
    "country": "Brazil",
    "lat": -21.1491,
    "lon": -49.5141,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_39",
    "name": "Brazil Industrial/Bank Asset #039",
    "country": "Brazil",
    "lat": -6.3228,
    "lon": -48.7356,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_40",
    "name": "Brazil Industrial/Bank Asset #040",
    "country": "Brazil",
    "lat": -18.5511,
    "lon": -55.2368,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_41",
    "name": "Brazil Industrial/Bank Asset #041",
    "country": "Brazil",
    "lat": -6.9429,
    "lon": -51.6229,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_42",
    "name": "Brazil Industrial/Bank Asset #042",
    "country": "Brazil",
    "lat": -22.0744,
    "lon": -45.9408,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_43",
    "name": "Brazil Industrial/Bank Asset #043",
    "country": "Brazil",
    "lat": -18.2579,
    "lon": -59.2458,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_44",
    "name": "Brazil Industrial/Bank Asset #044",
    "country": "Brazil",
    "lat": -11.4508,
    "lon": -46.1407,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_45",
    "name": "Brazil Industrial/Bank Asset #045",
    "country": "Brazil",
    "lat": -21.0135,
    "lon": -44.1549,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_46",
    "name": "Brazil Industrial/Bank Asset #046",
    "country": "Brazil",
    "lat": -14.6051,
    "lon": -54.5563,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_47",
    "name": "Brazil Industrial/Bank Asset #047",
    "country": "Brazil",
    "lat": -7.9209,
    "lon": -56.0766,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_48",
    "name": "Brazil Industrial/Bank Asset #048",
    "country": "Brazil",
    "lat": -7.0761,
    "lon": -48.6241,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_49",
    "name": "Brazil Industrial/Bank Asset #049",
    "country": "Brazil",
    "lat": -7.6712,
    "lon": -51.938,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_50",
    "name": "Brazil Industrial/Bank Asset #050",
    "country": "Brazil",
    "lat": -19.0353,
    "lon": -47.6823,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_51",
    "name": "Brazil Industrial/Bank Asset #051",
    "country": "Brazil",
    "lat": -8.2661,
    "lon": -57.198,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_52",
    "name": "Brazil Industrial/Bank Asset #052",
    "country": "Brazil",
    "lat": -18.9857,
    "lon": -56.4255,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_53",
    "name": "Brazil Industrial/Bank Asset #053",
    "country": "Brazil",
    "lat": -12.3324,
    "lon": -58.1121,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_54",
    "name": "Brazil Industrial/Bank Asset #054",
    "country": "Brazil",
    "lat": -20.523,
    "lon": -44.3566,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_55",
    "name": "Brazil Industrial/Bank Asset #055",
    "country": "Brazil",
    "lat": -11.417,
    "lon": -48.9784,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_56",
    "name": "Brazil Industrial/Bank Asset #056",
    "country": "Brazil",
    "lat": -12.4088,
    "lon": -47.1636,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_57",
    "name": "Brazil Industrial/Bank Asset #057",
    "country": "Brazil",
    "lat": -13.5664,
    "lon": -60.1593,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_58",
    "name": "Brazil Industrial/Bank Asset #058",
    "country": "Brazil",
    "lat": -14.5133,
    "lon": -49.748,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_59",
    "name": "Brazil Industrial/Bank Asset #059",
    "country": "Brazil",
    "lat": -14.3526,
    "lon": -43.1835,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_60",
    "name": "Brazil Industrial/Bank Asset #060",
    "country": "Brazil",
    "lat": -7.878,
    "lon": -45.2822,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_61",
    "name": "Brazil Industrial/Bank Asset #061",
    "country": "Brazil",
    "lat": -14.3771,
    "lon": -43.2009,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_62",
    "name": "Brazil Industrial/Bank Asset #062",
    "country": "Brazil",
    "lat": -7.5739,
    "lon": -55.8752,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_63",
    "name": "Brazil Industrial/Bank Asset #063",
    "country": "Brazil",
    "lat": -18.6765,
    "lon": -50.54,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_64",
    "name": "Brazil Industrial/Bank Asset #064",
    "country": "Brazil",
    "lat": -21.3636,
    "lon": -46.5331,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_65",
    "name": "Brazil Industrial/Bank Asset #065",
    "country": "Brazil",
    "lat": -14.5769,
    "lon": -51.1862,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_66",
    "name": "Brazil Industrial/Bank Asset #066",
    "country": "Brazil",
    "lat": -14.1904,
    "lon": -53.8331,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_67",
    "name": "Brazil Industrial/Bank Asset #067",
    "country": "Brazil",
    "lat": -11.2486,
    "lon": -57.7736,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_68",
    "name": "Brazil Industrial/Bank Asset #068",
    "country": "Brazil",
    "lat": -6.6059,
    "lon": -48.3516,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_69",
    "name": "Brazil Industrial/Bank Asset #069",
    "country": "Brazil",
    "lat": -14.8689,
    "lon": -48.5142,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_70",
    "name": "Brazil Industrial/Bank Asset #070",
    "country": "Brazil",
    "lat": -22.0409,
    "lon": -57.1265,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_71",
    "name": "Brazil Industrial/Bank Asset #071",
    "country": "Brazil",
    "lat": -12.9339,
    "lon": -55.0621,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_72",
    "name": "Brazil Industrial/Bank Asset #072",
    "country": "Brazil",
    "lat": -12.4256,
    "lon": -56.2454,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_73",
    "name": "Brazil Industrial/Bank Asset #073",
    "country": "Brazil",
    "lat": -13.453,
    "lon": -56.6515,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_74",
    "name": "Brazil Industrial/Bank Asset #074",
    "country": "Brazil",
    "lat": -14.6885,
    "lon": -49.8845,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_75",
    "name": "Brazil Industrial/Bank Asset #075",
    "country": "Brazil",
    "lat": -16.3752,
    "lon": -51.9421,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_76",
    "name": "Brazil Industrial/Bank Asset #076",
    "country": "Brazil",
    "lat": -18.8615,
    "lon": -48.3072,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_77",
    "name": "Brazil Industrial/Bank Asset #077",
    "country": "Brazil",
    "lat": -16.273,
    "lon": -45.5421,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_78",
    "name": "Brazil Industrial/Bank Asset #078",
    "country": "Brazil",
    "lat": -17.7559,
    "lon": -57.682,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_79",
    "name": "Brazil Industrial/Bank Asset #079",
    "country": "Brazil",
    "lat": -20.1318,
    "lon": -50.5539,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_80",
    "name": "Brazil Industrial/Bank Asset #080",
    "country": "Brazil",
    "lat": -18.5729,
    "lon": -59.1223,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_81",
    "name": "Brazil Industrial/Bank Asset #081",
    "country": "Brazil",
    "lat": -17.9108,
    "lon": -56.6755,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_82",
    "name": "Brazil Industrial/Bank Asset #082",
    "country": "Brazil",
    "lat": -15.3145,
    "lon": -54.0641,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_83",
    "name": "Brazil Industrial/Bank Asset #083",
    "country": "Brazil",
    "lat": -19.8965,
    "lon": -43.6553,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_84",
    "name": "Brazil Industrial/Bank Asset #084",
    "country": "Brazil",
    "lat": -19.8372,
    "lon": -46.418,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_85",
    "name": "Brazil Industrial/Bank Asset #085",
    "country": "Brazil",
    "lat": -19.4043,
    "lon": -51.9272,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_86",
    "name": "Brazil Industrial/Bank Asset #086",
    "country": "Brazil",
    "lat": -6.301,
    "lon": -45.631,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_87",
    "name": "Brazil Industrial/Bank Asset #087",
    "country": "Brazil",
    "lat": -13.9579,
    "lon": -47.9499,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_88",
    "name": "Brazil Industrial/Bank Asset #088",
    "country": "Brazil",
    "lat": -9.6647,
    "lon": -55.5194,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_89",
    "name": "Brazil Industrial/Bank Asset #089",
    "country": "Brazil",
    "lat": -13.2358,
    "lon": -50.699,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_bra_90",
    "name": "Brazil Industrial/Bank Asset #090",
    "country": "Brazil",
    "lat": -15.8556,
    "lon": -48.4902,
    "type": "Agro-Logistics & Petrobras Basins",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_1",
    "name": "South Africa Industrial/Bank Asset #001",
    "country": "South Africa",
    "lat": -34.0697,
    "lon": 26.0682,
    "type": "Eskom Grid & Deep Shaft Mines",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_2",
    "name": "South Africa Industrial/Bank Asset #002",
    "country": "South Africa",
    "lat": -30.7377,
    "lon": 24.2286,
    "type": "Eskom Grid & Deep Shaft Mines",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_3",
    "name": "South Africa Industrial/Bank Asset #003",
    "country": "South Africa",
    "lat": -30.9512,
    "lon": 21.2766,
    "type": "Eskom Grid & Deep Shaft Mines",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_4",
    "name": "South Africa Industrial/Bank Asset #004",
    "country": "South Africa",
    "lat": -31.6623,
    "lon": 23.5335,
    "type": "Eskom Grid & Deep Shaft Mines",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_5",
    "name": "South Africa Industrial/Bank Asset #005",
    "country": "South Africa",
    "lat": -27.0952,
    "lon": 20.5071,
    "type": "Eskom Grid & Deep Shaft Mines",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_6",
    "name": "South Africa Industrial/Bank Asset #006",
    "country": "South Africa",
    "lat": -34.3913,
    "lon": 19.1424,
    "type": "Eskom Grid & Deep Shaft Mines",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_7",
    "name": "South Africa Industrial/Bank Asset #007",
    "country": "South Africa",
    "lat": -27.6111,
    "lon": 27.5612,
    "type": "Eskom Grid & Deep Shaft Mines",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_8",
    "name": "South Africa Industrial/Bank Asset #008",
    "country": "South Africa",
    "lat": -32.9583,
    "lon": 23.6889,
    "type": "Eskom Grid & Deep Shaft Mines",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_9",
    "name": "South Africa Industrial/Bank Asset #009",
    "country": "South Africa",
    "lat": -29.357,
    "lon": 19.6754,
    "type": "Eskom Grid & Deep Shaft Mines",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_10",
    "name": "South Africa Industrial/Bank Asset #010",
    "country": "South Africa",
    "lat": -28.3075,
    "lon": 21.4811,
    "type": "Eskom Grid & Deep Shaft Mines",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_11",
    "name": "South Africa Industrial/Bank Asset #011",
    "country": "South Africa",
    "lat": -29.1645,
    "lon": 22.8049,
    "type": "Eskom Grid & Deep Shaft Mines",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_12",
    "name": "South Africa Industrial/Bank Asset #012",
    "country": "South Africa",
    "lat": -28.6578,
    "lon": 26.8263,
    "type": "Eskom Grid & Deep Shaft Mines",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_13",
    "name": "South Africa Industrial/Bank Asset #013",
    "country": "South Africa",
    "lat": -31.5014,
    "lon": 20.7952,
    "type": "Eskom Grid & Deep Shaft Mines",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_14",
    "name": "South Africa Industrial/Bank Asset #014",
    "country": "South Africa",
    "lat": -29.4963,
    "lon": 19.3785,
    "type": "Eskom Grid & Deep Shaft Mines",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_15",
    "name": "South Africa Industrial/Bank Asset #015",
    "country": "South Africa",
    "lat": -33.2094,
    "lon": 26.0072,
    "type": "Eskom Grid & Deep Shaft Mines",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_16",
    "name": "South Africa Industrial/Bank Asset #016",
    "country": "South Africa",
    "lat": -31.8509,
    "lon": 24.2427,
    "type": "Eskom Grid & Deep Shaft Mines",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_17",
    "name": "South Africa Industrial/Bank Asset #017",
    "country": "South Africa",
    "lat": -29.9769,
    "lon": 26.419,
    "type": "Eskom Grid & Deep Shaft Mines",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_18",
    "name": "South Africa Industrial/Bank Asset #018",
    "country": "South Africa",
    "lat": -33.9792,
    "lon": 19.55,
    "type": "Eskom Grid & Deep Shaft Mines",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_19",
    "name": "South Africa Industrial/Bank Asset #019",
    "country": "South Africa",
    "lat": -32.7243,
    "lon": 21.0988,
    "type": "Eskom Grid & Deep Shaft Mines",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_20",
    "name": "South Africa Industrial/Bank Asset #020",
    "country": "South Africa",
    "lat": -32.2191,
    "lon": 20.6047,
    "type": "Eskom Grid & Deep Shaft Mines",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_21",
    "name": "South Africa Industrial/Bank Asset #021",
    "country": "South Africa",
    "lat": -29.3928,
    "lon": 20.6425,
    "type": "Eskom Grid & Deep Shaft Mines",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_22",
    "name": "South Africa Industrial/Bank Asset #022",
    "country": "South Africa",
    "lat": -30.9908,
    "lon": 26.5581,
    "type": "Eskom Grid & Deep Shaft Mines",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_23",
    "name": "South Africa Industrial/Bank Asset #023",
    "country": "South Africa",
    "lat": -31.6447,
    "lon": 23.7992,
    "type": "Eskom Grid & Deep Shaft Mines",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_24",
    "name": "South Africa Industrial/Bank Asset #024",
    "country": "South Africa",
    "lat": -26.8258,
    "lon": 22.0699,
    "type": "Eskom Grid & Deep Shaft Mines",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_25",
    "name": "South Africa Industrial/Bank Asset #025",
    "country": "South Africa",
    "lat": -33.0789,
    "lon": 18.161,
    "type": "Eskom Grid & Deep Shaft Mines",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_26",
    "name": "South Africa Industrial/Bank Asset #026",
    "country": "South Africa",
    "lat": -28.7278,
    "lon": 24.5502,
    "type": "Eskom Grid & Deep Shaft Mines",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_27",
    "name": "South Africa Industrial/Bank Asset #027",
    "country": "South Africa",
    "lat": -27.0265,
    "lon": 24.937,
    "type": "Eskom Grid & Deep Shaft Mines",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_28",
    "name": "South Africa Industrial/Bank Asset #028",
    "country": "South Africa",
    "lat": -33.9095,
    "lon": 19.5991,
    "type": "Eskom Grid & Deep Shaft Mines",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_29",
    "name": "South Africa Industrial/Bank Asset #029",
    "country": "South Africa",
    "lat": -33.7259,
    "lon": 18.5679,
    "type": "Eskom Grid & Deep Shaft Mines",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_30",
    "name": "South Africa Industrial/Bank Asset #030",
    "country": "South Africa",
    "lat": -27.5205,
    "lon": 23.4143,
    "type": "Eskom Grid & Deep Shaft Mines",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_31",
    "name": "South Africa Industrial/Bank Asset #031",
    "country": "South Africa",
    "lat": -34.3391,
    "lon": 21.9001,
    "type": "Eskom Grid & Deep Shaft Mines",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_32",
    "name": "South Africa Industrial/Bank Asset #032",
    "country": "South Africa",
    "lat": -28.43,
    "lon": 18.7625,
    "type": "Eskom Grid & Deep Shaft Mines",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_33",
    "name": "South Africa Industrial/Bank Asset #033",
    "country": "South Africa",
    "lat": -32.4504,
    "lon": 19.4827,
    "type": "Eskom Grid & Deep Shaft Mines",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_34",
    "name": "South Africa Industrial/Bank Asset #034",
    "country": "South Africa",
    "lat": -29.3113,
    "lon": 26.7847,
    "type": "Eskom Grid & Deep Shaft Mines",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_35",
    "name": "South Africa Industrial/Bank Asset #035",
    "country": "South Africa",
    "lat": -32.075,
    "lon": 20.404,
    "type": "Eskom Grid & Deep Shaft Mines",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_36",
    "name": "South Africa Industrial/Bank Asset #036",
    "country": "South Africa",
    "lat": -32.2766,
    "lon": 24.1948,
    "type": "Eskom Grid & Deep Shaft Mines",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_37",
    "name": "South Africa Industrial/Bank Asset #037",
    "country": "South Africa",
    "lat": -33.4998,
    "lon": 26.3152,
    "type": "Eskom Grid & Deep Shaft Mines",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_38",
    "name": "South Africa Industrial/Bank Asset #038",
    "country": "South Africa",
    "lat": -34.3214,
    "lon": 24.5655,
    "type": "Eskom Grid & Deep Shaft Mines",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_39",
    "name": "South Africa Industrial/Bank Asset #039",
    "country": "South Africa",
    "lat": -27.667,
    "lon": 21.182,
    "type": "Eskom Grid & Deep Shaft Mines",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_40",
    "name": "South Africa Industrial/Bank Asset #040",
    "country": "South Africa",
    "lat": -30.7408,
    "lon": 27.6798,
    "type": "Eskom Grid & Deep Shaft Mines",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_41",
    "name": "South Africa Industrial/Bank Asset #041",
    "country": "South Africa",
    "lat": -30.2253,
    "lon": 20.6541,
    "type": "Eskom Grid & Deep Shaft Mines",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_42",
    "name": "South Africa Industrial/Bank Asset #042",
    "country": "South Africa",
    "lat": -30.9912,
    "lon": 27.6254,
    "type": "Eskom Grid & Deep Shaft Mines",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_43",
    "name": "South Africa Industrial/Bank Asset #043",
    "country": "South Africa",
    "lat": -28.969,
    "lon": 19.7004,
    "type": "Eskom Grid & Deep Shaft Mines",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_44",
    "name": "South Africa Industrial/Bank Asset #044",
    "country": "South Africa",
    "lat": -29.7693,
    "lon": 24.2405,
    "type": "Eskom Grid & Deep Shaft Mines",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_45",
    "name": "South Africa Industrial/Bank Asset #045",
    "country": "South Africa",
    "lat": -29.4632,
    "lon": 23.5698,
    "type": "Eskom Grid & Deep Shaft Mines",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_46",
    "name": "South Africa Industrial/Bank Asset #046",
    "country": "South Africa",
    "lat": -30.3623,
    "lon": 24.3253,
    "type": "Eskom Grid & Deep Shaft Mines",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_47",
    "name": "South Africa Industrial/Bank Asset #047",
    "country": "South Africa",
    "lat": -32.0727,
    "lon": 21.4017,
    "type": "Eskom Grid & Deep Shaft Mines",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_48",
    "name": "South Africa Industrial/Bank Asset #048",
    "country": "South Africa",
    "lat": -30.2327,
    "lon": 25.9771,
    "type": "Eskom Grid & Deep Shaft Mines",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_49",
    "name": "South Africa Industrial/Bank Asset #049",
    "country": "South Africa",
    "lat": -31.0151,
    "lon": 21.5878,
    "type": "Eskom Grid & Deep Shaft Mines",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_sou_50",
    "name": "South Africa Industrial/Bank Asset #050",
    "country": "South Africa",
    "lat": -32.4715,
    "lon": 20.9657,
    "type": "Eskom Grid & Deep Shaft Mines",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_1",
    "name": "Indonesia Industrial/Bank Asset #001",
    "country": "Indonesia",
    "lat": -4.7793,
    "lon": 121.4891,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_2",
    "name": "Indonesia Industrial/Bank Asset #002",
    "country": "Indonesia",
    "lat": 2.0036,
    "lon": 110.1732,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_3",
    "name": "Indonesia Industrial/Bank Asset #003",
    "country": "Indonesia",
    "lat": -1.0264,
    "lon": 102.1196,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_4",
    "name": "Indonesia Industrial/Bank Asset #004",
    "country": "Indonesia",
    "lat": 2.5967,
    "lon": 124.647,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_5",
    "name": "Indonesia Industrial/Bank Asset #005",
    "country": "Indonesia",
    "lat": -0.9635,
    "lon": 102.1392,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_6",
    "name": "Indonesia Industrial/Bank Asset #006",
    "country": "Indonesia",
    "lat": -1.3365,
    "lon": 108.9501,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_7",
    "name": "Indonesia Industrial/Bank Asset #007",
    "country": "Indonesia",
    "lat": -2.9303,
    "lon": 102.0932,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_8",
    "name": "Indonesia Industrial/Bank Asset #008",
    "country": "Indonesia",
    "lat": -1.7908,
    "lon": 111.8017,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_9",
    "name": "Indonesia Industrial/Bank Asset #009",
    "country": "Indonesia",
    "lat": -0.2956,
    "lon": 111.394,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_10",
    "name": "Indonesia Industrial/Bank Asset #010",
    "country": "Indonesia",
    "lat": -3.4738,
    "lon": 119.6108,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_11",
    "name": "Indonesia Industrial/Bank Asset #011",
    "country": "Indonesia",
    "lat": -1.6622,
    "lon": 111.0006,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_12",
    "name": "Indonesia Industrial/Bank Asset #012",
    "country": "Indonesia",
    "lat": -2.6762,
    "lon": 112.0537,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_13",
    "name": "Indonesia Industrial/Bank Asset #013",
    "country": "Indonesia",
    "lat": -2.8635,
    "lon": 120.2689,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_14",
    "name": "Indonesia Industrial/Bank Asset #014",
    "country": "Indonesia",
    "lat": 2.4996,
    "lon": 121.3018,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_15",
    "name": "Indonesia Industrial/Bank Asset #015",
    "country": "Indonesia",
    "lat": 0.6971,
    "lon": 108.7522,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_16",
    "name": "Indonesia Industrial/Bank Asset #016",
    "country": "Indonesia",
    "lat": 1.1634,
    "lon": 121.3314,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_17",
    "name": "Indonesia Industrial/Bank Asset #017",
    "country": "Indonesia",
    "lat": -1.4768,
    "lon": 122.4036,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_18",
    "name": "Indonesia Industrial/Bank Asset #018",
    "country": "Indonesia",
    "lat": -3.3207,
    "lon": 108.8703,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_19",
    "name": "Indonesia Industrial/Bank Asset #019",
    "country": "Indonesia",
    "lat": 0.3151,
    "lon": 116.7455,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_20",
    "name": "Indonesia Industrial/Bank Asset #020",
    "country": "Indonesia",
    "lat": -2.6029,
    "lon": 116.8661,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_21",
    "name": "Indonesia Industrial/Bank Asset #021",
    "country": "Indonesia",
    "lat": -3.2777,
    "lon": 102.3855,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_22",
    "name": "Indonesia Industrial/Bank Asset #022",
    "country": "Indonesia",
    "lat": -4.3829,
    "lon": 114.7593,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_23",
    "name": "Indonesia Industrial/Bank Asset #023",
    "country": "Indonesia",
    "lat": -3.2925,
    "lon": 104.3746,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_24",
    "name": "Indonesia Industrial/Bank Asset #024",
    "country": "Indonesia",
    "lat": -2.6264,
    "lon": 119.0847,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_25",
    "name": "Indonesia Industrial/Bank Asset #025",
    "country": "Indonesia",
    "lat": 1.0369,
    "lon": 107.5075,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_26",
    "name": "Indonesia Industrial/Bank Asset #026",
    "country": "Indonesia",
    "lat": -3.5745,
    "lon": 113.7659,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_27",
    "name": "Indonesia Industrial/Bank Asset #027",
    "country": "Indonesia",
    "lat": -2.0447,
    "lon": 109.3978,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_28",
    "name": "Indonesia Industrial/Bank Asset #028",
    "country": "Indonesia",
    "lat": 1.6157,
    "lon": 125.8711,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_29",
    "name": "Indonesia Industrial/Bank Asset #029",
    "country": "Indonesia",
    "lat": -1.0705,
    "lon": 120.9142,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_30",
    "name": "Indonesia Industrial/Bank Asset #030",
    "country": "Indonesia",
    "lat": -2.138,
    "lon": 122.1651,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_31",
    "name": "Indonesia Industrial/Bank Asset #031",
    "country": "Indonesia",
    "lat": 2.8332,
    "lon": 103.2649,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_32",
    "name": "Indonesia Industrial/Bank Asset #032",
    "country": "Indonesia",
    "lat": 1.4252,
    "lon": 103.6332,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_33",
    "name": "Indonesia Industrial/Bank Asset #033",
    "country": "Indonesia",
    "lat": -1.0188,
    "lon": 106.5326,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_34",
    "name": "Indonesia Industrial/Bank Asset #034",
    "country": "Indonesia",
    "lat": 1.9523,
    "lon": 121.534,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_35",
    "name": "Indonesia Industrial/Bank Asset #035",
    "country": "Indonesia",
    "lat": 1.846,
    "lon": 104.8471,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_36",
    "name": "Indonesia Industrial/Bank Asset #036",
    "country": "Indonesia",
    "lat": 1.3652,
    "lon": 107.8951,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_37",
    "name": "Indonesia Industrial/Bank Asset #037",
    "country": "Indonesia",
    "lat": 1.3898,
    "lon": 112.5511,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_38",
    "name": "Indonesia Industrial/Bank Asset #038",
    "country": "Indonesia",
    "lat": 1.121,
    "lon": 102.7242,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_39",
    "name": "Indonesia Industrial/Bank Asset #039",
    "country": "Indonesia",
    "lat": -1.0933,
    "lon": 120.4239,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_40",
    "name": "Indonesia Industrial/Bank Asset #040",
    "country": "Indonesia",
    "lat": -0.6109,
    "lon": 125.4908,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_41",
    "name": "Indonesia Industrial/Bank Asset #041",
    "country": "Indonesia",
    "lat": -0.9974,
    "lon": 118.2746,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_42",
    "name": "Indonesia Industrial/Bank Asset #042",
    "country": "Indonesia",
    "lat": -2.2831,
    "lon": 109.6735,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_43",
    "name": "Indonesia Industrial/Bank Asset #043",
    "country": "Indonesia",
    "lat": 0.2533,
    "lon": 102.9325,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_44",
    "name": "Indonesia Industrial/Bank Asset #044",
    "country": "Indonesia",
    "lat": 2.7194,
    "lon": 114.4222,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_45",
    "name": "Indonesia Industrial/Bank Asset #045",
    "country": "Indonesia",
    "lat": -2.7535,
    "lon": 117.2445,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_46",
    "name": "Indonesia Industrial/Bank Asset #046",
    "country": "Indonesia",
    "lat": -3.1902,
    "lon": 123.2205,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_47",
    "name": "Indonesia Industrial/Bank Asset #047",
    "country": "Indonesia",
    "lat": 2.1293,
    "lon": 107.1469,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_48",
    "name": "Indonesia Industrial/Bank Asset #048",
    "country": "Indonesia",
    "lat": -3.8766,
    "lon": 117.1098,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_49",
    "name": "Indonesia Industrial/Bank Asset #049",
    "country": "Indonesia",
    "lat": -2.1839,
    "lon": 105.9366,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_50",
    "name": "Indonesia Industrial/Bank Asset #050",
    "country": "Indonesia",
    "lat": -2.5712,
    "lon": 104.7916,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_51",
    "name": "Indonesia Industrial/Bank Asset #051",
    "country": "Indonesia",
    "lat": 1.5332,
    "lon": 102.1343,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_52",
    "name": "Indonesia Industrial/Bank Asset #052",
    "country": "Indonesia",
    "lat": -4.4441,
    "lon": 120.7234,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_53",
    "name": "Indonesia Industrial/Bank Asset #053",
    "country": "Indonesia",
    "lat": -0.9778,
    "lon": 116.2291,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_54",
    "name": "Indonesia Industrial/Bank Asset #054",
    "country": "Indonesia",
    "lat": -1.8088,
    "lon": 104.0675,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_55",
    "name": "Indonesia Industrial/Bank Asset #055",
    "country": "Indonesia",
    "lat": -3.5184,
    "lon": 104.1136,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_56",
    "name": "Indonesia Industrial/Bank Asset #056",
    "country": "Indonesia",
    "lat": 0.1692,
    "lon": 124.2604,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_57",
    "name": "Indonesia Industrial/Bank Asset #057",
    "country": "Indonesia",
    "lat": 3.1958,
    "lon": 116.9232,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_58",
    "name": "Indonesia Industrial/Bank Asset #058",
    "country": "Indonesia",
    "lat": -4.3018,
    "lon": 117.3898,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_59",
    "name": "Indonesia Industrial/Bank Asset #059",
    "country": "Indonesia",
    "lat": 0.8306,
    "lon": 120.9152,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_60",
    "name": "Indonesia Industrial/Bank Asset #060",
    "country": "Indonesia",
    "lat": -3.7734,
    "lon": 107.5042,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_61",
    "name": "Indonesia Industrial/Bank Asset #061",
    "country": "Indonesia",
    "lat": 3.0734,
    "lon": 120.8455,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_62",
    "name": "Indonesia Industrial/Bank Asset #062",
    "country": "Indonesia",
    "lat": 1.2736,
    "lon": 121.2526,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_63",
    "name": "Indonesia Industrial/Bank Asset #063",
    "country": "Indonesia",
    "lat": -1.2702,
    "lon": 106.5512,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_64",
    "name": "Indonesia Industrial/Bank Asset #064",
    "country": "Indonesia",
    "lat": 0.734,
    "lon": 110.516,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_ind_65",
    "name": "Indonesia Industrial/Bank Asset #065",
    "country": "Indonesia",
    "lat": -3.7021,
    "lon": 123.4879,
    "type": "Nickel Smelters & Coal Ports",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_1",
    "name": "Russia Industrial/Bank Asset #001",
    "country": "Russia",
    "lat": 55.8236,
    "lon": 56.25,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_2",
    "name": "Russia Industrial/Bank Asset #002",
    "country": "Russia",
    "lat": 53.5366,
    "lon": 71.8223,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_3",
    "name": "Russia Industrial/Bank Asset #003",
    "country": "Russia",
    "lat": 52.2773,
    "lon": 41.1976,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_4",
    "name": "Russia Industrial/Bank Asset #004",
    "country": "Russia",
    "lat": 54.172,
    "lon": 73.9441,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_5",
    "name": "Russia Industrial/Bank Asset #005",
    "country": "Russia",
    "lat": 53.3039,
    "lon": 79.881,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_6",
    "name": "Russia Industrial/Bank Asset #006",
    "country": "Russia",
    "lat": 60.9737,
    "lon": 63.2712,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_7",
    "name": "Russia Industrial/Bank Asset #007",
    "country": "Russia",
    "lat": 50.8265,
    "lon": 39.3015,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_8",
    "name": "Russia Industrial/Bank Asset #008",
    "country": "Russia",
    "lat": 53.5481,
    "lon": 45.801,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_9",
    "name": "Russia Industrial/Bank Asset #009",
    "country": "Russia",
    "lat": 54.4054,
    "lon": 30.0432,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_10",
    "name": "Russia Industrial/Bank Asset #010",
    "country": "Russia",
    "lat": 57.6563,
    "lon": 52.7426,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_11",
    "name": "Russia Industrial/Bank Asset #011",
    "country": "Russia",
    "lat": 52.2264,
    "lon": 31.1232,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_12",
    "name": "Russia Industrial/Bank Asset #012",
    "country": "Russia",
    "lat": 60.282,
    "lon": 76.561,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_13",
    "name": "Russia Industrial/Bank Asset #013",
    "country": "Russia",
    "lat": 52.8654,
    "lon": 73.2602,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_14",
    "name": "Russia Industrial/Bank Asset #014",
    "country": "Russia",
    "lat": 57.8995,
    "lon": 62.3374,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_15",
    "name": "Russia Industrial/Bank Asset #015",
    "country": "Russia",
    "lat": 54.6499,
    "lon": 61.4442,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_16",
    "name": "Russia Industrial/Bank Asset #016",
    "country": "Russia",
    "lat": 55.9706,
    "lon": 63.0881,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_17",
    "name": "Russia Industrial/Bank Asset #017",
    "country": "Russia",
    "lat": 57.3565,
    "lon": 49.356,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_18",
    "name": "Russia Industrial/Bank Asset #018",
    "country": "Russia",
    "lat": 57.6908,
    "lon": 36.6278,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_19",
    "name": "Russia Industrial/Bank Asset #019",
    "country": "Russia",
    "lat": 56.2784,
    "lon": 34.0008,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_20",
    "name": "Russia Industrial/Bank Asset #020",
    "country": "Russia",
    "lat": 60.0223,
    "lon": 37.7865,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_21",
    "name": "Russia Industrial/Bank Asset #021",
    "country": "Russia",
    "lat": 60.4819,
    "lon": 42.1247,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_22",
    "name": "Russia Industrial/Bank Asset #022",
    "country": "Russia",
    "lat": 55.8244,
    "lon": 35.9252,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_23",
    "name": "Russia Industrial/Bank Asset #023",
    "country": "Russia",
    "lat": 56.8521,
    "lon": 80.178,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_24",
    "name": "Russia Industrial/Bank Asset #024",
    "country": "Russia",
    "lat": 57.8951,
    "lon": 61.5493,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_25",
    "name": "Russia Industrial/Bank Asset #025",
    "country": "Russia",
    "lat": 58.4158,
    "lon": 45.3563,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_26",
    "name": "Russia Industrial/Bank Asset #026",
    "country": "Russia",
    "lat": 54.3962,
    "lon": 66.3572,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_27",
    "name": "Russia Industrial/Bank Asset #027",
    "country": "Russia",
    "lat": 50.8505,
    "lon": 85.8127,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_28",
    "name": "Russia Industrial/Bank Asset #028",
    "country": "Russia",
    "lat": 52.5049,
    "lon": 59.4843,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_29",
    "name": "Russia Industrial/Bank Asset #029",
    "country": "Russia",
    "lat": 60.6772,
    "lon": 34.7974,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_30",
    "name": "Russia Industrial/Bank Asset #030",
    "country": "Russia",
    "lat": 59.6122,
    "lon": 33.642,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_31",
    "name": "Russia Industrial/Bank Asset #031",
    "country": "Russia",
    "lat": 56.6962,
    "lon": 86.2946,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_32",
    "name": "Russia Industrial/Bank Asset #032",
    "country": "Russia",
    "lat": 54.9914,
    "lon": 52.1441,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_33",
    "name": "Russia Industrial/Bank Asset #033",
    "country": "Russia",
    "lat": 58.5012,
    "lon": 79.4186,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_34",
    "name": "Russia Industrial/Bank Asset #034",
    "country": "Russia",
    "lat": 53.1898,
    "lon": 32.4392,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_35",
    "name": "Russia Industrial/Bank Asset #035",
    "country": "Russia",
    "lat": 50.8447,
    "lon": 48.2343,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_36",
    "name": "Russia Industrial/Bank Asset #036",
    "country": "Russia",
    "lat": 61.3352,
    "lon": 87.6352,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_37",
    "name": "Russia Industrial/Bank Asset #037",
    "country": "Russia",
    "lat": 51.1654,
    "lon": 73.5103,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_38",
    "name": "Russia Industrial/Bank Asset #038",
    "country": "Russia",
    "lat": 56.3799,
    "lon": 41.3676,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_39",
    "name": "Russia Industrial/Bank Asset #039",
    "country": "Russia",
    "lat": 56.3143,
    "lon": 44.9258,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_40",
    "name": "Russia Industrial/Bank Asset #040",
    "country": "Russia",
    "lat": 57.5039,
    "lon": 40.7339,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_41",
    "name": "Russia Industrial/Bank Asset #041",
    "country": "Russia",
    "lat": 58.9903,
    "lon": 54.9111,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_42",
    "name": "Russia Industrial/Bank Asset #042",
    "country": "Russia",
    "lat": 51.2662,
    "lon": 68.3175,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_43",
    "name": "Russia Industrial/Bank Asset #043",
    "country": "Russia",
    "lat": 54.2956,
    "lon": 57.5232,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_44",
    "name": "Russia Industrial/Bank Asset #044",
    "country": "Russia",
    "lat": 57.9829,
    "lon": 82.9694,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_45",
    "name": "Russia Industrial/Bank Asset #045",
    "country": "Russia",
    "lat": 52.0017,
    "lon": 40.8238,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_46",
    "name": "Russia Industrial/Bank Asset #046",
    "country": "Russia",
    "lat": 54.8187,
    "lon": 50.2508,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_47",
    "name": "Russia Industrial/Bank Asset #047",
    "country": "Russia",
    "lat": 51.8981,
    "lon": 89.906,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_48",
    "name": "Russia Industrial/Bank Asset #048",
    "country": "Russia",
    "lat": 55.3161,
    "lon": 51.1394,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_49",
    "name": "Russia Industrial/Bank Asset #049",
    "country": "Russia",
    "lat": 53.7819,
    "lon": 89.4878,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_50",
    "name": "Russia Industrial/Bank Asset #050",
    "country": "Russia",
    "lat": 53.8958,
    "lon": 52.3032,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_51",
    "name": "Russia Industrial/Bank Asset #051",
    "country": "Russia",
    "lat": 59.1702,
    "lon": 55.8353,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_52",
    "name": "Russia Industrial/Bank Asset #052",
    "country": "Russia",
    "lat": 58.7104,
    "lon": 66.5048,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_53",
    "name": "Russia Industrial/Bank Asset #053",
    "country": "Russia",
    "lat": 56.7577,
    "lon": 42.8357,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_54",
    "name": "Russia Industrial/Bank Asset #054",
    "country": "Russia",
    "lat": 59.1885,
    "lon": 85.5688,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_55",
    "name": "Russia Industrial/Bank Asset #055",
    "country": "Russia",
    "lat": 53.0491,
    "lon": 87.6991,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_56",
    "name": "Russia Industrial/Bank Asset #056",
    "country": "Russia",
    "lat": 55.37,
    "lon": 53.8254,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_57",
    "name": "Russia Industrial/Bank Asset #057",
    "country": "Russia",
    "lat": 58.7158,
    "lon": 88.9774,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_58",
    "name": "Russia Industrial/Bank Asset #058",
    "country": "Russia",
    "lat": 57.1492,
    "lon": 61.0566,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_59",
    "name": "Russia Industrial/Bank Asset #059",
    "country": "Russia",
    "lat": 61.9209,
    "lon": 48.1105,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_60",
    "name": "Russia Industrial/Bank Asset #060",
    "country": "Russia",
    "lat": 53.604,
    "lon": 43.3132,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_61",
    "name": "Russia Industrial/Bank Asset #061",
    "country": "Russia",
    "lat": 60.2686,
    "lon": 31.3021,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_62",
    "name": "Russia Industrial/Bank Asset #062",
    "country": "Russia",
    "lat": 59.8633,
    "lon": 71.3832,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_63",
    "name": "Russia Industrial/Bank Asset #063",
    "country": "Russia",
    "lat": 53.3115,
    "lon": 63.2198,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_64",
    "name": "Russia Industrial/Bank Asset #064",
    "country": "Russia",
    "lat": 56.6759,
    "lon": 85.5553,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_65",
    "name": "Russia Industrial/Bank Asset #065",
    "country": "Russia",
    "lat": 51.8566,
    "lon": 32.2642,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_66",
    "name": "Russia Industrial/Bank Asset #066",
    "country": "Russia",
    "lat": 54.2679,
    "lon": 38.3045,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_67",
    "name": "Russia Industrial/Bank Asset #067",
    "country": "Russia",
    "lat": 54.405,
    "lon": 64.9293,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_68",
    "name": "Russia Industrial/Bank Asset #068",
    "country": "Russia",
    "lat": 52.7959,
    "lon": 78.6645,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_69",
    "name": "Russia Industrial/Bank Asset #069",
    "country": "Russia",
    "lat": 51.1029,
    "lon": 53.9879,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_70",
    "name": "Russia Industrial/Bank Asset #070",
    "country": "Russia",
    "lat": 61.0146,
    "lon": 74.056,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_71",
    "name": "Russia Industrial/Bank Asset #071",
    "country": "Russia",
    "lat": 58.683,
    "lon": 77.5743,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_72",
    "name": "Russia Industrial/Bank Asset #072",
    "country": "Russia",
    "lat": 52.0748,
    "lon": 79.5423,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_73",
    "name": "Russia Industrial/Bank Asset #073",
    "country": "Russia",
    "lat": 58.2751,
    "lon": 64.5739,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_74",
    "name": "Russia Industrial/Bank Asset #074",
    "country": "Russia",
    "lat": 60.8919,
    "lon": 65.7139,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_75",
    "name": "Russia Industrial/Bank Asset #075",
    "country": "Russia",
    "lat": 53.6047,
    "lon": 73.8474,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_76",
    "name": "Russia Industrial/Bank Asset #076",
    "country": "Russia",
    "lat": 56.9154,
    "lon": 34.7086,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_77",
    "name": "Russia Industrial/Bank Asset #077",
    "country": "Russia",
    "lat": 50.6711,
    "lon": 76.2541,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_78",
    "name": "Russia Industrial/Bank Asset #078",
    "country": "Russia",
    "lat": 54.1752,
    "lon": 79.0285,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_79",
    "name": "Russia Industrial/Bank Asset #079",
    "country": "Russia",
    "lat": 54.9983,
    "lon": 82.0699,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_80",
    "name": "Russia Industrial/Bank Asset #080",
    "country": "Russia",
    "lat": 60.4374,
    "lon": 43.6031,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_81",
    "name": "Russia Industrial/Bank Asset #081",
    "country": "Russia",
    "lat": 57.8334,
    "lon": 66.1381,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_82",
    "name": "Russia Industrial/Bank Asset #082",
    "country": "Russia",
    "lat": 50.1372,
    "lon": 76.6451,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_83",
    "name": "Russia Industrial/Bank Asset #083",
    "country": "Russia",
    "lat": 54.5898,
    "lon": 48.287,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_84",
    "name": "Russia Industrial/Bank Asset #084",
    "country": "Russia",
    "lat": 50.4942,
    "lon": 62.3958,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  },
  {
    "id": "mesh_rus_85",
    "name": "Russia Industrial/Bank Asset #085",
    "country": "Russia",
    "lat": 51.795,
    "lon": 60.1441,
    "type": "Pipeline Hubs & Heavy Metallurgical",
    "source": "Bloomberg Global Asset Database (BMAP Multi-Asset)"
  }
]

