import Header from "./scenes/Header";

function App() {
  return (
    <div className="app bg-opaque-black">
      <Header />
      <div className="flex justify-center items-center h-screen">
        <h1 className="font-playfair text-5xl font-bold text-blue-500">
          Making Readmes Just Got Simpler
        </h1>
      </div>
    </div>
  );
}

export default App;
