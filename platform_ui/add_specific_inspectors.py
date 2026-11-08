import os

js_path = 'F:/documents/SOIC/EconAgent_Platform/platform_ui/bmap_js_template.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

target_generic_else = '''    } else {
      // Generic facility / seaport / refinery / cavern
      nameEl.textContent = '● ' + item.name;'''

replacement_specific_infra = '''    } else if (type === 'power_plants' || (item && item.type && item.type.indexOf('Power') >= 0)) {
      nameEl.textContent = '⚡ ' + item.name;
      typeEl.textContent = 'Power Generation Utility';
      typeEl.style.background = '#451a03';
      typeEl.style.color = '#f59e0b';

      if (l1) l1.textContent = 'Grid Status:';
      statEl.textContent = '● Synchronized / Active Generation';
      statEl.style.color = '#00e676';

      if (l2) l2.textContent = 'Country / Region:';
      imoEl.textContent = item.country || 'Global Power Grid';

      if (l3) l3.textContent = 'Fuel / Technology:';
      ownerEl.textContent = item.type || 'Nuclear / Combined-Cycle Gas';

      if (l4) l4.textContent = 'Rated Capacity:';
      destEl.textContent = item.capacity || '2,400 MW';
      destEl.style.color = '#f59e0b';

      if (l5) l5.textContent = 'Dispatch Hierarchy:';
      berthEl.textContent = 'Base-Load Strategic Facility';

      if (l6) l6.textContent = 'Telemetry:';
      speedEl.textContent = 'Online Load 96.8% · 50/60 Hz Stable';
      speedEl.style.color = '#00e676';

      if (l7) l7.textContent = 'WGS84 Coordinates:';
      draftEl.textContent = item.lat.toFixed(4) + '°, ' + item.lon.toFixed(4) + '°';
    } else if (type === 'refineries' || (item && item.type && item.type.indexOf('Refin') >= 0)) {
      nameEl.textContent = '🏭 ' + item.name;
      typeEl.textContent = 'Crude Refining Complex';
      typeEl.style.background = '#450a0a';
      typeEl.style.color = '#ef4444';

      if (l1) l1.textContent = 'Refinery Status:';
      statEl.textContent = '● Operational Refining Units Active';
      statEl.style.color = '#00e676';

      if (l2) l2.textContent = 'Country / Basin:';
      imoEl.textContent = item.country || 'Major Hydrocarbon Hub';

      if (l3) l3.textContent = 'Processing Units:';
      ownerEl.textContent = 'CDU / VDU / Hydrocracker / FCCU';

      if (l4) l4.textContent = 'Throughput Capacity:';
      destEl.textContent = item.capacity || '550,000 bpd';
      destEl.style.color = '#ef4444';

      if (l5) l5.textContent = 'Complexity:';
      berthEl.textContent = 'Nelson Complexity Index 11.2 (High Conversion)';

      if (l6) l6.textContent = 'Product Slates:';
      speedEl.textContent = 'ULSD, Jet A-1, Gasoline, Petrochem Naphtha';
      speedEl.style.color = '#38bdf8';

      if (l7) l7.textContent = 'WGS84 Coordinates:';
      draftEl.textContent = item.lat.toFixed(4) + '°, ' + item.lon.toFixed(4) + '°';
    } else if (type === 'seaports' || (item && item.type && item.type.indexOf('Port') >= 0)) {
      nameEl.textContent = '⚓ ' + item.name;
      typeEl.textContent = 'Strategic Deepwater Port';
      typeEl.style.background = '#064e3b';
      typeEl.style.color = '#10b981';

      if (l1) l1.textContent = 'Port Authority:';
      statEl.textContent = '● Open / Vessel Navigation Active';
      statEl.style.color = '#00e676';

      if (l2) l2.textContent = 'Country / Region:';
      imoEl.textContent = item.country || 'Maritime Coastal Hub';

      if (l3) l3.textContent = 'Terminal Type:';
      ownerEl.textContent = item.type || 'Deepwater Oil & Container Terminal';

      if (l4) l4.textContent = 'Annual Throughput:';
      destEl.textContent = item.capacity || '180,000,000 MT / yr';
      destEl.style.color = '#10b981';

      if (l5) l5.textContent = 'Max Berth Draft:';
      berthEl.textContent = '22.5m (VLCC & Ultra Large Capesize Capable)';

      if (l6) l6.textContent = 'Current Traffic:';
      speedEl.textContent = 'Berth Utilization 89.4% · Minimal Waiting';
      speedEl.style.color = '#00e676';

      if (l7) l7.textContent = 'WGS84 Coordinates:';
      draftEl.textContent = item.lat.toFixed(4) + '°, ' + item.lon.toFixed(4) + '°';
    } else {
      // Generic facility / seaport / refinery / cavern
      nameEl.textContent = '● ' + item.name;'''

assert target_generic_else in js, "target_generic_else not found"
js = js.replace(target_generic_else, replacement_specific_infra, 1)

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)

print("Added bespoke inspectors for power plants, refineries, and seaports!")

