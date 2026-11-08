with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\fractal_zoom_engine.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Fix populateSectorDropdown: only target zoom_sector_select
target1 = "['zoom_sector_select', 'global_sector_select'].forEach(function(sId)"
repl1 = "['zoom_sector_select'].forEach(function(sId)"
if target1 in code:
    code = code.replace(target1, repl1)
    print("Replaced target1")

# 2. Fix populateCompanyDropdown: only target zoom_firm_select
target2 = "['zoom_firm_select', 'global_firm_select'].forEach(function(sId)"
repl2 = "['zoom_firm_select'].forEach(function(sId)"
if target2 in code:
    code = code.replace(target2, repl2)
    print("Replaced target2")

# 3. Fix syncGlobalRibbon
target3 = """function syncGlobalRibbon() {
    var gc = document.getElementById('global_country_select');
    var gs = document.getElementById('global_sector_select');
    var gf = document.getElementById('global_firm_select');
    var gn = document.getElementById('global_nano_select');

    if (gc && gc.value !== currentCountry) gc.value = currentCountry;
    if (gs && countryData[currentCountry]) {
      gs.innerHTML = '';
      countryData[currentCountry].sectors.forEach(function(sKey) {
        var s = sectorData[sKey];
        if (s) {
          var o = document.createElement('option');
          o.value = sKey;
          o.textContent = s.name;
          gs.appendChild(o);
        }
      });
      gs.value = currentSector;
    }
    if (gf && sectorData[currentSector] && sectorData[currentSector].firmKeys) {
      gf.innerHTML = '';
      sectorData[currentSector].firmKeys.forEach(function(fKey) {
        var f = firmData[fKey];
        if (f) {
          var o = document.createElement('option');
          o.value = fKey;
          o.textContent = f.name + ' [' + f.ticker + ']';
          gf.appendChild(o);
        }
      });
      gf.value = currentFirm;
    }
    if (gn && firmData[currentFirm]) {
      gn.innerHTML = '';
      var f = firmData[currentFirm];
      if (f.nanoLink && nanoData[f.nanoLink]) {
        var o = document.createElement('option');
        o.value = f.nanoLink;
        o.textContent = nanoData[f.nanoLink].title;
        gn.appendChild(o);
      }
      var oDom = document.createElement('option');
      oDom.value = 'dom';
      oDom.textContent = '📊 Level 2 Order Book (DOM Microstructure)';
      gn.appendChild(oDom);
      gn.value = currentNano;
    }
  }"""

repl3 = """function syncGlobalRibbon() {
    var gc = document.getElementById('global_country_select');
    var gf = document.getElementById('global_firm_select');

    // Only update selection if matching option exists; never wipe out master 94-industry options
    if (gc && Array.from(gc.options).some(function(o) { return o.value === currentCountry; })) {
      gc.value = currentCountry;
    }
    if (gf && Array.from(gf.options).some(function(o) { return o.value === currentFirm; })) {
      gf.value = currentFirm;
    }
  }"""

assert target3 in code, "target3 not found in fractal_zoom_engine.py"
code = code.replace(target3, repl3)
print("Replaced target3")

with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\fractal_zoom_engine.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("fractal_zoom_engine.py patched successfully!")
