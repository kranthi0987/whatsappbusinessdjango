import React, {Component} from 'react';
import {Link} from 'react-router-dom';
import toaster from "toasted-notes";
import "toasted-notes/src/styles.css";
import {
    Button,
    Card,
    CardBody,
    CardGroup,
    Col,
    Container,
    Form,
    Input,
    InputGroup,
    InputGroupAddon,
    InputGroupText,
    Row
} from 'reactstrap';

class Login extends Component {
    constructor() {

        super();
        this.state = {
            username: '',
            password: '',
            submitted: false,
            loading: false,
            error: ''
        };
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }


    handleChange(e) {
        const {name, value} = e.target;
        this.setState({[name]: value});
    }

    handleSubmit(e) {
        e.preventDefault();

        this.setState({submitted: true});
        const {username, password, returnUrl} = this.state;

        // stop here if form is invalid
        if (!(username && password)) {
            return;
        }
        console.log(username, password);

        this.setState({loading: true});

        let url = 'http://127.0.0.1:8000/api/auth/login';

        fetch(url, {
            method: "POST",
            headers: ({
                "Accept": "application/json",
                "Content-Type": "application/json"
            }),
            body: JSON.stringify({
                username: username,
                password: password
            })
        }).then(response => {
            if (response.status === 200) {
                console.log(response);
                toaster.notify("Sucessfull logged in", {
                    duration: 2000, type: "success"
                });
                this.props.history.push('/dashboard')
                return response.json()
            } else {
                toaster.notify("failed login", {
                    duration: 2000, type: "error"
                });
                console.log("oh no!", response.status === 404)
            }
        }).then(function (data) {
            localStorage.setItem("token", data.token);
            // toaster.notify("Hello world", {
            //     duration: 2000
            // });
            console.log('request succeeded with JSON response', data)
        })
    }


    render() {
        const {username, password, submitted, loading, error} = this.state;
        return (
            <div className="app flex-row align-items-center">
                <Container>
                    <Row className="justify-content-center">
                        <Col md="8">
                            <CardGroup>
                                <Card className="p-4">
                                    <CardBody>
                                        <Form>
                                            <h1>Login</h1>
                                            <p className="text-muted">Sign In to your account</p>
                                            <InputGroup className="mb-3">
                                                <InputGroupAddon addonType="prepend">
                                                    <InputGroupText>
                                                        <i className="icon-user"></i>
                                                    </InputGroupText>
                                                </InputGroupAddon>
                                                <Input type="text" placeholder="Username" autoComplete="username"
                                                       name="username" value={username} onChange={this.handleChange}/>
                                                {submitted && !username &&
                                                <div className="help-block">Username is required</div>
                                                }
                                            </InputGroup>
                                            <InputGroup className="mb-4">
                                                <InputGroupAddon addonType="prepend">
                                                    <InputGroupText>
                                                        <i className="icon-lock"></i>
                                                    </InputGroupText>
                                                </InputGroupAddon>
                                                <Input type="password" placeholder="Password"
                                                       autoComplete="current-password" name="password" value={password}
                                                       onChange={this.handleChange}/>
                                                {submitted && !password &&
                                                <div className="help-block">Password is required</div>
                                                }
                                            </InputGroup>
                                            <Row>
                                                <Col xs="6">
                                                    <Button color="primary" className="px-4"
                                                            onClick={this.handleSubmit}>Login</Button>
                                                </Col>
                                                <Col xs="6" className="text-right">
                                                    <Button color="link" className="px-0">Forgot password?</Button>
                                                </Col>
                                            </Row>
                                        </Form>
                                    </CardBody>
                                </Card>
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
                            </CardGroup>
                        </Col>
                    </Row>
                </Container>
            </div>
        );
    }
}

export default Login;
