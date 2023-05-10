import { FaGithub } from "react-icons/fa";

export default function Header() {
  return (
    <nav className="z-40 w-full fixed top-0 py-6 bg-blue-900 text-white">
      <div className="flex items-center justify-between mx-auto w-5/6">
        <h4 className="font-playfair text-3xl font-bold text-white">Readme Generator</h4>
        <div className="flex justify-between gap-8">
          <a href="#" className="text-white hover:text-blue-200">Home</a>
          <a href="#" className="text-white hover:text-blue-200">About</a>
          <a
            href="https://github.com/Chaitanyarai899/GithubReadmeGenerator"
            target="_blank"
            rel="noopener noreferrer"
            className="hover:text-white hover:bg-blue-700 rounded-full p-1"
          >
            <FaGithub size={32} />
          </a>
        </div>
      </div>
    </nav>
  );
}
