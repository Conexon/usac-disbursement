import { useState, useRef, useEffect } from 'react';
import mapboxgl from 'mapbox-gl';

const Map = () => {
  const [theMap, setTheMap] = useState(null);
  const mapDiv = useRef(null);

  useEffect(() => {
    mapboxgl.accessToken =
      'pk.eyJ1IjoiY29uZXhvbi1kZXNpZ24iLCJhIjoiY2pvdzZlb2djMXVhOTN3bmhpYzk3NndoZCJ9.On4IrAd0sgmmgd_sAqg_Gg';

    const map = new mapboxgl.Map({
      container: mapDiv.current,
      hash: true,
      style: 'mapbox://styles/conexon-design/cjow6vt3sax7q2rpbj5wm7s84',
      center: [-91.96, 38.02],
      minZoom: 4,
      maxZoom: 10,
      zoom: 4,
    });

    setTheMap(map);
    //}
    // remove the map when component unmounts
    return function cleanUp() {
      map.remove();
    };
  }, []);

  useEffect(() => {
    if (theMap) {
      const sac_remain_URL = 'mapbox://conexon-design.sac_remain';
      const sac_remain_SourceLayer = 'sac_remain';
      const unserved_1_URL = 'mapbox://conexon-design.unserved_1';
      const unserved_1_SourceLayer = 'unserved_1';
      const unserved_2_URL = 'mapbox://conexon-design.unserved_2';
      const unserved_2_SourceLayer = 'unserved_2';
      const unserved_3_URL = 'mapbox://conexon-design.unserved_3';
      const unserved_3_SourceLayer = 'unserved_3';
      const unserved_4_URL = 'mapbox://conexon-design.unserved_4';
      const unserved_4_SourceLayer = 'unserved_4';
      const unserved_5_URL = 'mapbox://conexon-design.unserved_5';
      const unserved_5_SourceLayer = 'unserved_5';
      const unserved_6_URL = 'mapbox://conexon-design.unserved_6';
      const unserved_6_SourceLayer = 'unserved_6';
      const SACUrl = 'mapbox://conexon-design.sac';
      const SACSourceLayer = 'sac';

      const unservedFill = '#FFA500';
      const blackBorder = '#000000';
      const SACFill = '#0000FF';
      const SACSelectFill = '#0000FF';
      theMap.on('load', function () {
        //the unaccoutned for sac remain
        theMap.addLayer({
          id: 'sac_remain',
          type: 'fill',
          source: {
            type: 'vector',
            url: sac_remain_URL,
          },
          'source-layer': sac_remain_SourceLayer,
          // filter: ['>', 'fcc_904', 0],
          paint: {
            'fill-color': unservedFill,
            'fill-opacity': 0.1,
            'fill-outline-color': blackBorder,
          },
          layout: {
            visibility: 'visible',
          },
        });
        //unserved layer
        theMap.addLayer({
          id: 'unserved_1',
          type: 'fill',
          source: {
            type: 'vector',
            url: unserved_1_URL,
          },
          'source-layer': unserved_1_SourceLayer,
          // filter: ['>', 'fcc_904', 0],
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
            url: unserved_2_URL,
          },
          'source-layer': unserved_2_SourceLayer,
          // filter: ['>', 'fcc_904', 0],
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
            url: unserved_3_URL,
          },
          'source-layer': unserved_3_SourceLayer,
          // filter: ['>', 'fcc_904', 0],
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
            url: unserved_4_URL,
          },
          'source-layer': unserved_4_SourceLayer,
          // filter: ['>', 'fcc_904', 0],
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
            url: unserved_5_URL,
          },
          'source-layer': unserved_5_SourceLayer,
          // filter: ['>', 'fcc_904', 0],
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
            url: unserved_6_URL,
          },
          'source-layer': unserved_6_SourceLayer,
          // filter: ['>', 'fcc_904', 0],
          paint: {
            'fill-color': unservedFill,
            'fill-opacity': 0.7,
            'fill-outline-color': blackBorder,
          },
          layout: {
            visibility: 'visible',
          },
        });

        //SAC layer
        theMap.addLayer({
          id: 'sac_poly',
          type: 'fill',
          source: {
            type: 'vector',
            url: SACUrl,
          },
          'source-layer': SACSourceLayer,
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
            url: SACUrl,
          },
          'source-layer': SACSourceLayer,
          paint: {
            'line-color': SACFill,
            'line-width': 1.1,
          },
          layout: {
            visibility: 'visible',
          },
        });
      });
    }
  }, [theMap]);

  return (
    <div
      id="map"
      ref={mapDiv}
      className="w-full max-w-full"
      style={{ height: '600px' }}
    ></div>
  );
};

export default Map;
