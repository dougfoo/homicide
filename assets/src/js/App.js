import React from 'react';
import { Table, message } from 'antd';
import { Menu, Icon } from 'antd';
import { Typography } from 'antd';
import 'antd/dist/antd.css';
import axios from 'axios';
import './App.css';

const { SubMenu } = Menu;
const { Title, Text } = Typography;

class Map extends React.Component {
  render() {
    return (
      <script type="text/javascript" src="https://homicidestorage.z13.web.core.windows.net/homicide.1.js"></script>
    )
  }
}

class MyHomicides extends React.Component {
  state = { 
    visible: false,
    homicides: [],
    current: 'mail',
  };

  handleClick = e => {
    console.log('click ', e);
    this.setState({
      current: e.key,
    });
  };

  componentDidMount() {
    console.log('consolemount');
    try {
      axios.get('/homicides/').then(response => response.data)
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
        <Title>Homicide: Life on the Street in Charlotte - 2019</Title>
        <Menu onClick={this.handleClick} selectedKeys={[this.state.current]} mode="horizontal">
          <Menu.Item key="home">
            <Icon type="team" />
            Home
          </Menu.Item>
          <Menu.Item key="charts">
            <Icon type="pie-chart" />
            Analytics / Charts
          </Menu.Item>
          <Menu.Item key="maps">
            <Icon type="car" />
            Maps
          </Menu.Item>
          <Menu.Item key="about">
            <Icon type="question-circle" />
              About
          </Menu.Item>
        </Menu>
        { this.state.current == 'home' && <Table columns={columns} expandedRowRender={record => <p style={{ margin: 0 }}>{record.means}</p>} dataSource={data} /> }
        { this.state.current == 'charts' && <div>Chart Page</div> }
        { this.state.current == 'maps' && <div>Map Render Page</div> }
        { this.state.current == 'about' && <div>About This App</div> }
        <Text code>(C) 2019 Foo Enterprises</Text>
    </div>
    )
  }
}

function App() {
  return (
    <div className="App">
      <MyHomicides/>
    </div>
  );
}

export default App;
