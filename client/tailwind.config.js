/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        blue: "#2CBCE9",
        red: "#FF6969",
        yellow: "#FFD93D",
        green: "#39FF14",
        grey: "#ededed",
        "deep-blue": "#010026",
        "dark-gray": "#5A5A5A",
        "opaque-black": "rgba(0, 0, 0, 0.35)",
      },
      backgroundImage: (theme) => ({
        "gradient-yellow":
          "linear-gradient(87.4deg, rgb(255, 241, 165) 1.9%, rgb(200, 125, 76) 49.7%, rgb(83, 54, 54) 100.5%)",
        "gradient-black":
          "linear-gradient(109.6deg, rgb(36, 45, 57) 11.2%, rgb(16, 37, 60) 51.2%, rgb(0, 0, 0) 98.6%)",
      }),
      fontFamily: {
        playfair: ["Playfair Display", "serif"],
      },
      content: {},
    },
    screens: {
      xs: "480px",
      sm: "768px",
      md: "1060px",
    },
  },
  plugins: [],
};
