import React from 'react';
import { Table, message } from 'antd';
import axios from 'axios';
import './App.css';

class Foo extends React.Component {
  state = { 
    visible: false,
    homicides: [],
  }

  componentDidMount() {
    console.log('consolemount');
    try {
      axios.get('http://localhost:8000/homicides/').then(response => response.data)
          .then((data) => {
            console.log('homicides',data);
            this.setState({ homicides: data });
          })
          .catch(function (error) {
              message.error("Axios backend loans error: "+error);
          })
    } catch (error) {
      console.error(error);
      message.error("Axios unhandled error: "+error);
    } 
  }

  render() {
    const data = this.state.homicides;
    const columns = [
      {
        title: 'Date',
        dataIndex: 'date',
        key: 'date',
        render: text => <a href="/homicides/">{text}</a>,
      },
      { title: 'Name', dataIndex: 'name', key: 'name', },
      { title: 'Age', dataIndex: 'age', key: 'age', },
      { title: 'Gender', dataIndex: 'gender', key: 'gender', },
      { title: 'Ethnic', dataIndex: 'ethnicity', key: 'ethnicity', },
      { title: 'Means', dataIndex: 'means', key: 'means', },
      { title: 'Street', dataIndex: 'street', key: 'street', },
    ];

    return (
      <div>
        <span>
          Hello World
        </span>
        <Table columns={columns} expandedRowRender={record => <p style={{ margin: 0 }}>{record.description}</p>} dataSource={data} />,
      </div>
    )
  }
}

function App() {
  return (
    <div className="App">
      <Foo/>
    </div>
  );
}

export default App;
