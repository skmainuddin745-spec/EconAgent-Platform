with open(r"F:\documents\SOIC\EconAgent_Platform\platform_ui\generate_global_bmap_js.py", "r", encoding="utf-8") as f:
    code = f.read()

# Replace startLiveKinematicsEngine definition
old_engine = """  // ═══════════════════════════════════════════════════════════════
  // ── LIVE DEAD-RECKONING KINEMATICS ENGINE (2-SECOND TICK) ──
  // ═══════════════════════════════════════════════════════════════
  function startLiveKinematicsEngine() {
    if (liveKinematicsTimer) clearInterval(liveKinematicsTimer);

    liveKinematicsTimer = setInterval(function() {
      var dt = 2; // 2 seconds
      
      globalVessels.forEach(function(v) {
        if (v.speed > 0) {
          var speedMs = (v.speed * 1852) / 3600; // m/s
          var distMeters = speedMs * dt;
          var rad = (v.course * Math.PI) / 180;
          
          var dLat = (distMeters * Math.cos(rad)) / 111139;
          var dLon = (distMeters * Math.sin(rad)) / (111139 * Math.cos((v.lat * Math.PI) / 180));
          
          v.lat += dLat;
          v.lon += dLon;

          if (v.marker) {
            v.marker.setLatLng([v.lat, v.lon]);
          }
          if (v.headingLine && showArpaVectors) {
            var headingDist = v.speed * 0.008;
            var hLat = v.lat + headingDist * Math.cos(rad);
            var hLon = v.lon + (headingDist * Math.sin(rad)) / Math.cos(v.lat * Math.PI / 180);
            v.headingLine.setLatLngs([[v.lat, v.lon], [hLat, hLon]]);
          }
        }
      });

      // Auto-follow active vessel
      if (activeFollowVessel && leafletMap) {
        leafletMap.panTo([activeFollowVessel.lat, activeFollowVessel.lon], { animate: true, duration: 0.4 });
      }
    }, 2000);
  }"""

new_engine = """  // ═══════════════════════════════════════════════════════════════
  // ── LIVE DEAD-RECKONING KINEMATICS ENGINE (2-SECOND TICK) ──
  // ═══════════════════════════════════════════════════════════════
  window.bmapVessels = globalVessels;
  window.datasetLayerGroups = datasetLayerGroups;
  window.activeLayers = activeLayers;

  window.stepKinematics = function(dt) {
    dt = dt || 2;
    globalVessels.forEach(function(v) {
      if (v.speed > 0) {
        var speedMs = (v.speed * 1852) / 3600;
        var distMeters = speedMs * dt;
        var rad = (v.course * Math.PI) / 180;
        
        var dLat = (distMeters * Math.cos(rad)) / 111139;
        var dLon = (distMeters * Math.sin(rad)) / (111139 * Math.cos((v.lat * Math.PI) / 180));
        
        v.lat += dLat;
        v.lon += dLon;

        if (v.marker) {
          v.marker.setLatLng([v.lat, v.lon]);
        }
        if (v.headingLine && showArpaVectors) {
          var headingDist = v.speed * 0.008;
          var hLat = v.lat + headingDist * Math.cos(rad);
          var hLon = v.lon + (headingDist * Math.sin(rad)) / Math.cos(v.lat * Math.PI / 180);
          v.headingLine.setLatLngs([[v.lat, v.lon], [hLat, hLon]]);
        }
      }
    });

    if (activeFollowVessel && leafletMap) {
      leafletMap.panTo([activeFollowVessel.lat, activeFollowVessel.lon], { animate: true, duration: 0.4 });
    }
  };

  function startLiveKinematicsEngine() {
    if (liveKinematicsTimer) clearInterval(liveKinematicsTimer);
    liveKinematicsTimer = setInterval(function() {
      window.stepKinematics(2);
    }, 2000);
    window.liveKinematicsTimer = liveKinematicsTimer;
  }"""

# Note in generate_global_bmap_js.py, brackets are doubled: {{ and }}
# So let's replace appropriately
if "function startLiveKinematicsEngine() {{" in code:
    code = code.replace(
        "  function startLiveKinematicsEngine() {{\n    if (liveKinematicsTimer) clearInterval(liveKinematicsTimer);",
        "  window.bmapVessels = globalVessels;\n  window.datasetLayerGroups = datasetLayerGroups;\n  window.activeLayers = activeLayers;\n\n  window.stepKinematics = function(dt) {{\n    dt = dt || 2;\n    globalVessels.forEach(function(v) {{\n      if (v.speed > 0) {{\n        var speedMs = (v.speed * 1852) / 3600;\n        var distMeters = speedMs * dt;\n        var rad = (v.course * Math.PI) / 180;\n        var dLat = (distMeters * Math.cos(rad)) / 111139;\n        var dLon = (distMeters * Math.sin(rad)) / (111139 * Math.cos((v.lat * Math.PI) / 180));\n        v.lat += dLat;\n        v.lon += dLon;\n        if (v.marker) v.marker.setLatLng([v.lat, v.lon]);\n        if (v.headingLine && showArpaVectors) {{\n          var headingDist = v.speed * 0.008;\n          var hLat = v.lat + headingDist * Math.cos(rad);\n          var hLon = v.lon + (headingDist * Math.sin(rad)) / Math.cos(v.lat * Math.PI / 180);\n          v.headingLine.setLatLngs([[v.lat, v.lon], [hLat, hLon]]);\n        }}\n      }}\n    }});\n    if (activeFollowVessel && leafletMap) {{\n      leafletMap.panTo([activeFollowVessel.lat, activeFollowVessel.lon], {{ animate: true, duration: 0.4 }});\n    }}\n  }};\n\n  function startLiveKinematicsEngine() {{\n    if (liveKinematicsTimer) clearInterval(liveKinematicsTimer);\n    liveKinematicsTimer = setInterval(function() {{ window.stepKinematics(2); }}, 2000);\n    window.liveKinematicsTimer = liveKinematicsTimer;"
    )
    # Remove the old setInterval body
    old_body = """    liveKinematicsTimer = setInterval(function() {{
      var dt = 2; // 2 seconds
      
      globalVessels.forEach(function(v) {{
        if (v.speed > 0) {{
          var speedMs = (v.speed * 1852) / 3600; // m/s
          var distMeters = speedMs * dt;
          var rad = (v.course * Math.PI) / 180;
          
          var dLat = (distMeters * Math.cos(rad)) / 111139;
          var dLon = (distMeters * Math.sin(rad)) / (111139 * Math.cos((v.lat * Math.PI) / 180));
          
          v.lat += dLat;
          v.lon += dLon;

          if (v.marker) {{
            v.marker.setLatLng([v.lat, v.lon]);
          }}
          if (v.headingLine && showArpaVectors) {{
            var headingDist = v.speed * 0.008;
            var hLat = v.lat + headingDist * Math.cos(rad);
            var hLon = v.lon + (headingDist * Math.sin(rad)) / Math.cos(v.lat * Math.PI / 180);
            v.headingLine.setLatLngs([[v.lat, v.lon], [hLat, hLon]]);
          }}
        }}
      }});

      // Auto-follow active vessel
      if (activeFollowVessel && leafletMap) {{
        leafletMap.panTo([activeFollowVessel.lat, activeFollowVessel.lon], {{ animate: true, duration: 0.4 }});
      }}
    }}, 2000);"""
    code = code.replace(old_body, "")

with open(r"F:\documents\SOIC\EconAgent_Platform\platform_ui\generate_global_bmap_js.py", "w", encoding="utf-8") as f:
    f.write(code)

print("generate_global_bmap_js.py updated successfully.")

