import { saveAs } from 'file-saver';
import { sendLink } from "./services/api";
import { useState } from "react";
import { FaCamera } from "react-icons/fa6";
import './styles.css'


function App() {

  const [isFocused, setIsFocused] = useState(false);
  const[link, setLink] = useState();

  async function downloadImage(filename) {
    const url = 'http://127.0.0.1:5000/static/img/' + filename;
  
    try {
      const response = await fetch(url);
      if (!response.ok) {
        alert('Erro ao baixar imagem');
        return
      }
  
      const blob = await response.blob();
      saveAs(blob, 'Screenshot.jpg'); 
    } catch (error) {
      alert('Erro ao baixar imagem');
    }
  }
  
  async function verifyInput() {
    if (link === '') {
      alert('Adicione o link!');
      return;
    }
  
    const response = await sendLink(link);
    await downloadImage(response.success);
  }

  return (
    <div className="container">
        <div className="containerImg"><img src="logo.png" alt="" /></div>
        <div className="containerInput">
          <fieldset className={isFocused ? "focused" : ""}>
              <legend>Adicione o link</legend>
              <input
                type="text"
                placeholder="Adicione o link"
                onFocus={() => setIsFocused(true)}
                onBlur={() => setIsFocused(false)}
                onChange={(e)=> setLink(e.target.value)}
              />
              <button 
              className="buttonInput"
              onClick={verifyInput}>
                <FaCamera size={25} />
              </button>
          </fieldset>
      </div>
    </div>
  );
}

export default App;
