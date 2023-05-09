import { FaGithub } from "react-icons/fa";

export default function Header() {
  return (
    <nav className="z-40 w-full fixed top-0 py-6 text-green">
      <div className="flex items-center justify-between mx-auto w-5/6">
        <h4 className="font-playfair text-3xl font-bold">Readme Generator</h4>
        <div className="flex justify-between gap-8">
          <a href="#">Home</a>
          <a href="#">About</a>
          <a
            href="https://github.com/Chaitanyarai899/GithubReadmeGenerator"
            target="_blank"
            rel="noopener noreferrer"
            className="hover:text-white hover:bg-green rounded-full"
          >
            <FaGithub size={32} />
          </a>
        </div>
      </div>
    </nav>
  );
}
