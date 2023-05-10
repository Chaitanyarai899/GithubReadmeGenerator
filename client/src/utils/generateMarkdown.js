export function generateMarkdown(name, learning, talksAbout, otherDetails) {
    return `
  # Hey I am ${name} 
  
  ## About Me
  
  - 🌱 I’m currently learning ${learning}.
  - 💬 Ask me About ${talksAbout}
  - ${otherDetails ? otherDetails + '\n' : ''}
  
  ## My GitHub Stats
  
  ![My GitHub Stats](https://github-readme-stats.vercel.app/api?username=${name.toLowerCase()}&show_icons=true&count_private=true&hide=stars)
  
  ## My Top Languages
  
  ![My Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=${name.toLowerCase()}&layout=compact)
  `;
  }
  