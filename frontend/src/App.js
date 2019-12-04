import React, { Component } from 'react';
import './App.css';
import './index.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Card } from 'react-bootstrap';
import Navbar from './components/Navbar';

class App extends Component {
    state = {
        faangm: [],
    };

    async componentDidMount() {
        try {
            const res = await fetch('http://127.0.0.1:8000/faangm/');
            const faangm = await res.json();
            this.setState({
                faangm,
            });
        } catch (e) {
            console.log(e);
        }
    }

    render() {
        return (
            <div className="container">
                <Navbar />
                <br />
                <h1>Faangm Companies</h1>
                <p>See the list to understand what it means.</p>
                <p>Date format used: DD/MM/YYYY</p>
                {this.state.faangm.map(item => {
                    return (
                        <div className="row">
                            <div className="col-sm-12">
                                <Card style={{ margin: `10px` }}>
                                    <Card.Header
                                        style={{
                                            textAlign: `center`,
                                            fontSize: `18px`,
                                            fontWeight: `bold`,
                                        }}
                                    >
                                        Name: {item.name}
                                    </Card.Header>
                                    <Card.Body>
                                        <Card.Text
                                            style={{
                                                textAlign: `center`,
                                            }}
                                        >
                                            Created: {item.created}
                                        </Card.Text>
                                        <Card.Text
                                            style={{
                                                textAlign: `center`,
                                            }}
                                        >
                                            Founder(s):{' '}
                                            {item.founders}
                                        </Card.Text>
                                        <Card.Text
                                            style={{
                                                color: `red`,
                                                textAlign: `center`,
                                            }}
                                        >
                                            Location: {item.location}
                                        </Card.Text>
                                    </Card.Body>
                                </Card>
                            </div>
                        </div>
                    );
                })}
            </div>
        );
    }
}

export default App;
