import React, {Component} from 'react';
import {Button, Card, CardBody, CardGroup} from "reactstrap";
import {Link} from "react-router-dom";


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
                <Card className="text-white bg-primary py-5 d-md-down-none" style={{width: '44%'}}>
                    <CardBody className="text-center">
                        <div>
                            <h2>Register</h2>
                            <p>Register the account with all details to get the server</p>
                            <Link to="/register">
                                <Button color="primary" className="mt-3" active tabIndex={-1}>Register
                                    Now!</Button>
                            </Link>
                        </div>
                    </CardBody>
                </Card>
            </div>
        );
    }
}

export default Dashboard;
