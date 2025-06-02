# XYZ Tiles Basemap Loader

A QGIS plugin to quickly load multiple open-source basemaps as XYZ tiles with one click. Includes popular sources like OpenStreetMap, Google Maps, Esri, CartoDB, and more.

## Installation
1. Download the plugin ZIP file from the QGIS plugin repository.
2. In QGIS, go to `Plugins > Manage and Install Plugins > Install from ZIP`.
   
[![Diagram of the System](https://github.com/AnustupJana/xyzTilesBasemapLoader-plugin/blob/main/doc/1st%20Plugin.png?raw=true)](https://github.com/AnustupJana/xyzTilesBasemapLoader-plugin/blob/main/doc/1st%20Plugin.png?raw=true)

3. Select the downloaded ZIP file and install.

[![Diagram of the System](https://github.com/AnustupJana/xyzTilesBasemapLoader-plugin/blob/main/doc/2nd%20Install.png?raw=true)](https://github.com/AnustupJana/xyzTilesBasemapLoader-plugin/blob/main/doc/2nd%20Install.png?raw=true)

4. The plugin will appear in the QGIS toolbar and Plugins menu.

## Usage
1. Click the plugin icon or select `XYZ Tiles Basemap Loader` from the Plugins menu.

[![Diagram of the System](https://github.com/AnustupJana/xyzTilesBasemapLoader-plugin/blob/main/doc/3rd%20Add%20Base%20maps.png?raw=true)](https://github.com/AnustupJana/xyzTilesBasemapLoader-plugin/blob/main/doc/3rd%20Add%20Base%20maps.png?raw=true)

2. The plugin will automatically add basemaps to the QGIS Browser panel under `XYZ Tiles`.
3. A message will appear: "All base map add successfully. It is not show on xyz tiles please restart the QGIS."

[![Diagram of the System](https://github.com/AnustupJana/xyzTilesBasemapLoader-plugin/blob/main/doc/4th%20Show%20all%20Added%20base%20map.png?raw=true)]([https://github.com/AnustupJana/xyzTilesBasemapLoader-plugin/blob/main/doc/2nd%20Install.png](https://github.com/AnustupJana/xyzTilesBasemapLoader-plugin/blob/main/doc/4th%20Show%20all%20Added%20base%20map.png)?raw=true)

4. **Note**: In QGIS 3.40.17, you may need to restart QGIS to see the basemaps in the Browser panel. For QGIS 3.16, basemaps should appear immediately.

## Notes
- Some basemaps (e.g., Esri services) may require an ArcGIS Online subscription.
- Check the QGIS Browser panel for the loaded basemaps.
- Report issues or feature requests at the [issue tracker](https://github.com/AnustupJana/xyzTilesBasemapLoader-plugin/issues).

## License
This plugin is licensed under the GNU General Public License v2.0 or later.
