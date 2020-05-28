import { useState, useRef, useEffect } from 'react';
import mapboxgl from 'mapbox-gl';

import Content from '../components/Content';

const Map = () => {
  const [theMap, setTheMap] = useState(null);
  const mapDiv = useRef(null);
  const [highlightType, setHighlightType] = useState(null);
  const [properties, setProperties] = useState(null);

  useEffect(() => {
    mapboxgl.accessToken =
      'pk.eyJ1IjoiY29uZXhvbi1kZXNpZ24iLCJhIjoiY2pvdzZlb2djMXVhOTN3bmhpYzk3NndoZCJ9.On4IrAd0sgmmgd_sAqg_Gg';

    const map = new mapboxgl.Map({
      container: mapDiv.current,
      style: 'mapbox://styles/conexon-design/cjow6vt3sax7q2rpbj5wm7s84',
      center: [-96.25, 40],
      minZoom: 3.5,
      maxZoom: 10,
      zoom: 3.5,
    });

    setTheMap(map);

    return function cleanUp() {
      map.remove();
    };
  }, []);

  useEffect(() => {
    if (theMap) {
      const unservedFill = 'orange';
      const blackBorder = 'black';
      const SACFill = 'blue';
      const SACSelectFill = 'red';

      theMap.on('load', function () {
        theMap.addLayer({
          id: 'sac_remain',
          type: 'fill',
          source: {
            type: 'vector',
            url: 'mapbox://conexon-design.sac_remain',
          },
          'source-layer': 'sac_remain',
          paint: {
            'fill-color': unservedFill,
            'fill-opacity': 0.1,
            'fill-outline-color': blackBorder,
          },
          layout: {
            visibility: 'visible',
          },
        });

        theMap.addLayer({
          id: 'unserved_1',
          type: 'fill',
          source: {
            type: 'vector',
            url: 'mapbox://conexon-design.unserved_1',
          },
          'source-layer': 'unserved_1',
          paint: {
            'fill-color': unservedFill,
            'fill-opacity': 0.7,
            'fill-outline-color': blackBorder,
          },
          layout: {
            visibility: 'visible',
          },
        });

        theMap.addLayer({
          id: 'unserved_2',
          type: 'fill',
          source: {
            type: 'vector',
            url: 'mapbox://conexon-design.unserved_2',
          },
          'source-layer': 'unserved_2',
          paint: {
            'fill-color': unservedFill,
            'fill-opacity': 0.7,
            'fill-outline-color': blackBorder,
          },
          layout: {
            visibility: 'visible',
          },
        });

        theMap.addLayer({
          id: 'unserved_3',
          type: 'fill',
          source: {
            type: 'vector',
            url: 'mapbox://conexon-design.unserved_3',
          },
          'source-layer': 'unserved_3',
          paint: {
            'fill-color': unservedFill,
            'fill-opacity': 0.7,
            'fill-outline-color': blackBorder,
          },
          layout: {
            visibility: 'visible',
          },
        });

        theMap.addLayer({
          id: 'unserved_4',
          type: 'fill',
          source: {
            type: 'vector',
            url: 'mapbox://conexon-design.unserved_4',
          },
          'source-layer': 'unserved_4',
          paint: {
            'fill-color': unservedFill,
            'fill-opacity': 0.7,
            'fill-outline-color': blackBorder,
          },
          layout: {
            visibility: 'visible',
          },
        });

        theMap.addLayer({
          id: 'unserved_5',
          type: 'fill',
          source: {
            type: 'vector',
            url: 'mapbox://conexon-design.unserved_5',
          },
          'source-layer': 'unserved_5',
          paint: {
            'fill-color': unservedFill,
            'fill-opacity': 0.7,
            'fill-outline-color': blackBorder,
          },
          layout: {
            visibility: 'visible',
          },
        });

        theMap.addLayer({
          id: 'unserved_6',
          type: 'fill',
          source: {
            type: 'vector',
            url: 'mapbox://conexon-design.unserved_6',
          },
          'source-layer': 'unserved_6',
          paint: {
            'fill-color': unservedFill,
            'fill-opacity': 0.7,
            'fill-outline-color': blackBorder,
          },
          layout: {
            visibility: 'visible',
          },
        });

        theMap.addLayer({
          id: 'sac_poly',
          type: 'fill',
          source: {
            type: 'vector',
            url: 'mapbox://conexon-design.sac',
          },
          'source-layer': 'sac',
          paint: {
            'fill-color': SACFill,
            'fill-opacity': 0.1,
            'fill-outline-color': blackBorder,
          },
          layout: {
            visibility: 'visible',
          },
        });

        theMap.addLayer({
          id: 'SAC_Lines',
          type: 'line',
          source: {
            type: 'vector',
            url: 'mapbox://conexon-design.sac',
          },
          'source-layer': 'sac',
          paint: {
            'line-color': SACFill,
            'line-width': 1.1,
          },
          layout: {
            visibility: 'visible',
          },
        });
      });

      theMap.on('click', 'sac_poly', (event) => {
        console.log('poly', event.features[0].properties);
        theMap.setPaintProperty('sac_poly', 'fill-color', [
          'case',
          ['==', ['get', 'sac'], event.features[0].properties.sac],
          'red',
          SACSelectFill,
        ]);
        theMap.setPaintProperty('sac_poly', 'fill-opacity', [
          'case',
          ['==', ['get', 'sac'], event.features[0].properties.sac],
          0.4,
          0.1,
        ]);

        theMap.setPaintProperty('sac_remain', 'fill-color', unservedFill);
        theMap.setPaintProperty('sac_remain', 'fill-opacity', 0.1);

        setHighlightType('poly');
        setProperties(event.features[0].properties);
      });

      theMap.on('click', 'sac_remain', (event) => {
        console.log('remain', event.features[0].properties);
        theMap.setPaintProperty('sac_remain', 'fill-color', [
          'case',
          [
            '==',
            ['get', 'state_abbv'],
            event.features[0].properties.state_abbv,
          ],
          'red',
          SACSelectFill,
        ]);
        theMap.setPaintProperty('sac_remain', 'fill-opacity', [
          'case',
          [
            '==',
            ['get', 'state_abbv'],
            event.features[0].properties.state_abbv,
          ],
          0.8,
          0.1,
        ]);

        theMap.setPaintProperty('sac_poly', 'fill-color', SACSelectFill);
        theMap.setPaintProperty('sac_poly', 'fill-opacity', 0.1);

        setHighlightType('remain');
        setProperties(event.features[0].properties);
      });

      theMap.on('mouseenter', 'sac_poly', function () {
        theMap.getCanvas().style.cursor = 'pointer';
      });

      // Change it back to a pointer when it leaves.
      theMap.on('mouseleave', 'sac_poly', function () {
        theMap.getCanvas().style.cursor = '';
      });

      theMap.on('mouseenter', 'sac_remain', function () {
        theMap.getCanvas().style.cursor = 'pointer';
      });

      // Change it back to a pointer when it leaves.
      theMap.on('mouseleave', 'sac_remain', function () {
        theMap.getCanvas().style.cursor = '';
      });
    }
  }, [theMap]);

  console.log('Map ', highlightType);
  return (
    <div className="grid grid-cols-12">
      <div className="col-span-7">
        <div
          id="map"
          ref={mapDiv}
          className="w-full max-w-full min-h-screen"
        ></div>
      </div>

      <Content highlightType={highlightType} properties={properties} />
    </div>
  );
};

export default Map;
