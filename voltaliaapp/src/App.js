import './App.css';
import React, { useState, useEffect } from 'react';
import Table from './Table';

const App = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://127.0.0.1:5000/visualizar_dados');
        const jsonData = await response.json();
        setData(jsonData.casos);
      } catch (error) {
        console.error('Erro ao buscar dados da API:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <h1>Dados do Covid19</h1>
      <Table data={data} /> 
    </div>
  );
};

export default App;
