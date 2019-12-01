import React, {Component} from 'react';
import {Button, Card, CardBody, CardGroup, Col, Row} from "reactstrap";
import Widget04 from "../Widgets/Widget04";



class Dashboard extends Component {
    constructor(props) {
        super(props);
        // this.getwallpapers()
    }

    // getwallpapers(e) {
    //     // make API call
    //     this.setState({loading: true});
    //     let url = 'http://127.0.0.1:8000/wallpapers/listwallpapers/';
    //     fetch(url, {
    //         method: "GET",
    //         headers: ({
    //             "Authorization": "Token ".concat(localStorage.getItem('token'))
    //         })
    //     }).then(response => {
    //         if (response.status === 200) {
    //             console.log(response);
    //             return response.json()
    //         } else {
    //             console.log("oh no!", response.status === 404)
    //         }
    //     }).then(function (data) {
    //         console.log('request succeeded with JSON response', data)
    //     })
    // }

    render() {

        return (
            <div className="animated fadeIn">
                <CardGroup className="mb-4">
                    <Widget04 icon="icon-people" color="info" header="87.500" value="25">Visitors</Widget04>
                    <Widget04 icon="icon-user-follow" color="success" header="385" value="25">New Clients</Widget04>
                    <Widget04 icon="icon-basket-loaded" color="warning" header="1238" value="25">Products
                        sold</Widget04>
                    <Widget04 icon="icon-pie-chart" color="primary" header="28%" value="25">Returning
                        Visitors</Widget04>
                    <Widget04 icon="icon-speedometer" color="danger" header="5:34:11" value="25">Avg. Time</Widget04>
                </CardGroup>
                <Row>
                    <Col sm="6" md="2">
                        <Widget04 icon="icon-people" color="info" header="87.500" value="25" invert>Visitors</Widget04>
                    </Col>
                    <Col sm="6" md="2">
                        <Widget04 icon="icon-user-follow" color="success" header="385" value="25" invert>New
                            Clients</Widget04>
                    </Col>
                    <Col sm="6" md="2">
                        <Widget04 icon="icon-basket-loaded" color="warning" header="1238" value="25" invert>Products
                            sold</Widget04>
                    </Col>
                    <Col sm="6" md="2">
                        <Widget04 icon="icon-pie-chart" color="primary" header="28%" value="25" invert>Returning
                            Visitors</Widget04>
                    </Col>
                    <Col sm="6" md="2">
                        <Widget04 icon="icon-speedometer" color="danger" header="5:34:11" value="25" invert>Avg.
                            Time</Widget04>
                    </Col>
                    <Col sm="6" md="2">
                        <Widget04 icon="icon-speech" color="info" header="972" value="25" invert>Comments</Widget04>
                    </Col>
                </Row>
            </div>
        );
    }
}

export default Dashboard;
