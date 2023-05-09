import { useState } from 'react';
import ReactMarkdown from 'react-markdown';
import { generateMarkdown } from '@/utils/generateMarkdown';

function FormComponent() {
  const [name, setName] = useState('');
  const [learning, setLearning] = useState('');
  const [talksAbout, setTalksAbout] = useState('');
  const [otherDetails, setOtherDetails] = useState('');

  const handleNameChange = (event) => {
    setName(event.target.value);
  };

  const handleLearningChange = (event) => {
    setLearning(event.target.value);
  };

  const handleTalksAboutChange = (event) => {
    setTalksAbout(event.target.value);
  };

  const handleOtherDetailsChange = (event) => {
    setOtherDetails(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    const markdown = generateMarkdown(name, learning, talksAbout, otherDetails);
    setMarkdown(markdown);
  };

  const [markdown, setMarkdown] = useState('');

  return (
<div className="flex flex-row">
  <form className="w-1/2 p-4 bg-off-white">
    <div className="mb-4">
      <label className="block text-gray-700 font-bold mb-2" htmlFor="name">
        Github UserId
      </label>
      <input
        className="shadow appearance-none border rounded w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline bg-white text-dark-grey"
        id="name"
        type="text"
        placeholder="@username"
        value={name}
        onChange={handleNameChange}
      />
    </div>
    <div className="mb-4">
      <label className="block font-bold mb-2" htmlFor="learning">
        Currently Learning
      </label>
      <input
        className="shadow appearance-none border rounded w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline bg-white text-dark-grey"
        id="learning"
        type="text"
        placeholder="ReactJS"
        value={learning}
        onChange={handleLearningChange}
      />
    </div>
    <div className="mb-4">
      <label className="block font-bold mb-2" htmlFor="learning">
        Talks about
      </label>
      <input
        className="shadow appearance-none border rounded w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline bg-white text-dark-grey"
        id="learning"
        type="text"
        placeholder="ReactJS"
        value={talksAbout}
        onChange={handleTalksAboutChange}
      />
    </div>
    <div className="mb-4">
      <label className="block font-bold mb-2" htmlFor="other-details">
        Other Details
      </label>
      <textarea
        className="shadow appearance-none border rounded w-full py-2 px-3 text-dark-grey leading-tight focus:outline-none focus:shadow-outline bg-white"
        id="other-details"
        placeholder="Enter additional details here..."
        value={otherDetails}
        onChange={handleOtherDetailsChange}
      />
    </div>
    <button
      className="bg-black hover:bg-grey text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
      type="submit"
      onClick={handleSubmit}
    >
      Generate Readme
    </button>
  </form>
  <div className="w-1/2 p-4 bg-dark-grey text-white">
    <ReactMarkdown>{markdown}</ReactMarkdown>
  </div>
</div>


  );
}

export default FormComponent;
