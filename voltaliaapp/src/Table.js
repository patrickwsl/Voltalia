import React, { Component } from 'react';
import axios from 'axios';

class Table extends Component {
  state = {
    casos: [],
  };

  componentDidMount() {
    axios.get('http://127.0.0.1:5000/visualizar_dados')
      .then((response) => {
        this.setState({ casos: response.data.casos });
      })
      .catch((error) => {
        console.error('Erro ao buscar dados da API:', error);
      });
  }

  render() {
    const { casos } = this.state;

    return (
      <div className="container mt-5">
        <h1 className="mb-4">Formulário de Dados</h1>
        <table className="table table-striped">
          <thead>
            <tr>
              <th>Cidade</th>
              <th>Estado</th>
              <th>Data</th>
              <th>Novos Confirmados</th>
              <th>Novas Mortes</th>
            </tr>
          </thead>
          <tbody>
            {casos.map((caso, index) => (
              <tr key={index}>
                <td>{caso.city}</td>
                <td>{caso.state}</td>
                <td>{caso.date}</td>
                <td>{caso.new_confirmed}</td>
                <td>{caso.new_deaths}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    );
  }
}

export default Table;
