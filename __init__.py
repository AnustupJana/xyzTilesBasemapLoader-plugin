# -*- coding: utf-8 -*-
"""
/***************************************************************************
 XyzTilesBasemapLoader
                                 A QGIS plugin
 Quickly load multiple open-source basemaps as XYZ tiles with one click. Includes popular sources like OSM, Google, Bing, and more
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2025-06-02
        copyright            : (C) 2025 by Anustup Jana
        email                : anustupjana21@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load XyzTilesBasemapLoader class from file XyzTilesBasemapLoader.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .xyz_tiles_basemap_loader import XyzTilesBasemapLoader
    return XyzTilesBasemapLoader(iface)
