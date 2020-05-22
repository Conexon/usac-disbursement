import dynamic from 'next/dynamic';

const Map = dynamic(() => import('../components/Map'), {
  ssr: false,
});

const HomePage = () => {
  return <Map />;
};

export default HomePage;
