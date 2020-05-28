import Title from './Title';
import Intro from './Intro';

const RemainContent = ({ properties }) => {
  return (
    <div className="bg-white overflow-hidden shadow rounded-lg mt-8">
      <h2 className="border-b border-gray-200 px-4 py-5 sm:px-6 text-2xl">
        Unaccounted For Funds in {properties.state_name} 
      </h2>
      <div className="px-4 py-5 sm:p-6">
        <p className="mb-8">
          USAC reports and distributes money based on the Study Area Code (SAC)
          geography. There is no wall to wall publically avaialble dataset for
          SACs, leaving the public to guess at where these funds are meant to
          provide service. The red shaded area represents the unaccounted for
          funds presented below in{' '}
          <span className="font-semibold">{properties.state_name}</span>.
        </p>
        <table className="min-w-full">
          <tbody>
            <tr>
              <th className="px-6 py-3 border-b border-gray-200 bg-gray-50 text-left text-xs leading-4 font-medium text-gray-500 uppercase tracking-wider">
                Program
              </th>
              <th className="px-6 py-3 border-b border-gray-200 bg-gray-50 text-left text-xs leading-4 font-medium text-gray-500 uppercase tracking-wider">
                Amount Unaccounted for
              </th>
            </tr>
            <tr>
              <td className="px-6 py-4 whitespace-no-wrap border-b border-gray-200 text-sm leading-5 text-gray-900">
                High Cost
              </td>
              <td className="px-6 py-4 whitespace-no-wrap border-b border-gray-200 text-sm leading-5 font-medium text-gray-900">
                {properties.unacc_hc}
              </td>
            </tr>
            <tr>
              <td className="px-6 py-4 whitespace-no-wrap border-b border-gray-200 text-sm leading-5 text-gray-900">
                CAF
              </td>
              <td className="px-6 py-4 whitespace-no-wrap border-b border-gray-200 text-sm leading-5 font-medium text-gray-900">
                {properties.unacc_caf}
              </td>
            </tr>
            <tr>
              <td className="px-6 py-4 whitespace-no-wrap text-sm leading-5 text-gray-900 font-bold">
                Total
              </td>
              <td className="px-6 py-4 whitespace-no-wrap text-sm leading-5 font-medium text-gray-900 font-bold">
                {properties.total}
              </td>
            </tr>
            <tr>
              <td className="px-6 py-4 whitespace-no-wrap text-xs leading-5 text-gray-900">
                Number of SACs unaccounted for
              </td>
              <td className="px-6 py-4 whitespace-no-wrap text-xs leading-5 font-medium text-gray-900">
                {properties.num_sac}
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
};

const PolyContent = ({ properties }) => {
  return (
    <div className="bg-white overflow-hidden shadow rounded-lg mt-8">
      <h2 className="border-b border-gray-200 px-4 py-5 sm:px-6 text-2xl">
        {properties.co_lower}
      </h2>
      <div className="px-4 py-5 sm:p-6">
        <p className="mb-8">
          <span className="font-semibold">{properties.co_lower}</span> has
          received the federal support shown below to deliver broadband in the
          red shaded area. Even with this support, the orange shaded areas still
          lack access to basic broadband services, such as services that are
          widely available in urban and suburban areas.
        </p>
        <table className="min-w-full mb-8">
          <tbody>
            <tr>
              <th className="px-6 py-3 border-b border-gray-200 bg-gray-50 text-left text-xs leading-4 font-medium text-gray-500 uppercase tracking-wider">
                Program
              </th>
              <th className="px-6 py-3 border-b border-gray-200 bg-gray-50 text-left text-xs leading-4 font-medium text-gray-500 uppercase tracking-wider">
                Support since 2015
              </th>
            </tr>
            <tr>
              <td className="px-6 py-4 whitespace-no-wrap border-b border-gray-200 text-sm leading-5 text-gray-900">
                High Cost
              </td>
              <td className="px-6 py-4 whitespace-no-wrap border-b border-gray-200 text-sm leading-5 font-medium text-gray-900">
                {properties.high_cost}
              </td>
            </tr>
            <tr>
              <td className="px-6 py-4 whitespace-no-wrap border-b border-gray-200 text-sm leading-5 text-gray-900">
                CAF
              </td>
              <td className="px-6 py-4 whitespace-no-wrap border-b border-gray-200 text-sm leading-5 font-medium text-gray-900">
                {properties.caf}
              </td>
            </tr>
            <tr>
              <td className="px-6 py-4 whitespace-no-wrap text-sm leading-5 text-gray-900 font-bold">
                Total
              </td>
              <td className="px-6 py-4 whitespace-no-wrap text-sm leading-5 text-gray-900 font-bold">
                {properties.total}
              </td>
            </tr>
          </tbody>
        </table>
        <ul className="text-xs text-gray-900">
          <li>
            Source: The Universal Service Administrative Co Funding Disbursement
            Tool -{' '}
            <a className="text-blue-500" href="https://www.usac.org">
              https://www.usac.org
            </a>
          </li>
          <li>
            FCC Form 477 -{' '}
            <a className="text-blue-500" href="http://www.fcc.gov">
              http://www.fcc.gov
            </a>
          </li>
          <li>Unserved is defined as lacking Fiber or Cable (consumer) service</li>
          <li>
            How we made this map -{' '}
            <a className="text-blue-500" href="https://github.com/Conexon/usac-disbursement">
              https://github.com/Conexon/usac-disbursement
            </a>
          </li>          
        </ul>
      </div>
    </div>
  );
};

const Content = (props) => {
  return (
    <div className="col-span-5">
      <div className="m-8">
        <div className="mb-8">
          <a href="https://www.conexon.us/" title="Conexon.us">
            <img
              src="/conexon-logo-white.png"
              alt="Conexon"
              width="25px"
              className="inline"
            />{' '}
            <span className="font-semibold">conexon</span>
          </a>
        </div>
        <Title />
        <Intro />
        {props.highlightType === 'poly' && props.properties ? (
          <PolyContent properties={props.properties} />
        ) : props.highlightType === 'remain' && props.properties ? (
          <RemainContent properties={props.properties} />
        ) : null}
      </div>
    </div>
  );

  return null;
};

export default Content;
