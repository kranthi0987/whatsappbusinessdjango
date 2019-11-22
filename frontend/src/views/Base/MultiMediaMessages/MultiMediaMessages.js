import React, {Component} from 'react';
import {
    Badge,
    Button,
    Card,
    CardBody,
    CardFooter,
    CardHeader,
    Col,
    Collapse,
    DropdownItem,
    DropdownMenu,
    DropdownToggle,
    Fade,
    Form,
    FormGroup,
    FormText,
    FormFeedback,
    Input,
    InputGroup,
    InputGroupAddon,
    InputGroupButtonDropdown,
    InputGroupText,
    Label,
    Row,
} from 'reactstrap';
// Import React FilePond
import {FilePond, registerPlugin} from 'react-filepond';

// Import FilePond styles
import 'filepond/dist/filepond.min.css';
// Import the Image EXIF Orientation and Image Preview plugins
// Note: These need to be installed separately
import FilePondPluginImageExifOrientation from 'filepond-plugin-image-exif-orientation';
import FilePondPluginImagePreview from 'filepond-plugin-image-preview';
import 'filepond-plugin-image-preview/dist/filepond-plugin-image-preview.css';

import toaster from "toasted-notes";
import "toasted-notes/src/styles.css";
import {setOptions} from "filepond";

registerPlugin(FilePondPluginImagePreview, FilePondPluginImageExifOrientation);

class MultiMediaMessages extends Component {
    constructor(props) {
        super(props);

        this.toggle = this.toggle.bind(this);
        this.toggleFade = this.toggleFade.bind(this);
        this.state = {
            collapse: true,
            fadeIn: true,
            timeout: 300
        };
        this.state = {
            from_who: '9989015918',
            to_who: '',
            message_status: '',
            message: '',
            submitted: false,
            loading: false,
            error: ''
        };
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        setOptions({
            server: {
                url: 'http://localhost:8000',
                timeout: 7000,
                process: {
                    url: '/mediaupload/fileupload/',
                    method: 'POST',
                    headers: {},
                    withCredentials: false,
                    onload: (response) => console.log(response),
                    onerror: (response) => console.log(response.data),
                    // ondata: (formData) => {
                    //     formData.append('Hello', 'World');
                    //     return formData;
                    // }
                },
                // revert: './revert',
                // restore: './restore/',
                // load: './load/',
                // fetch: './fetch/'
            }
        });
    }

    toggle() {
        this.setState({collapse: !this.state.collapse});
    }

    toggleFade() {
        this.setState((prevState) => {
            return {fadeIn: !prevState}
        });
    }

    handleSubmit(e) {
        e.preventDefault();

        this.setState({submitted: true});
        const {from_who = ['9989015918'], to_who, message_status, message} = this.state;

        // stop here if form is invalid
        if (!(to_who && message)) {
            return;
        }
        console.log(to_who, message);

        this.setState({loading: true});

        let url = 'http://127.0.0.1:8000/message/multimediamessages/';


        let formData = new FormData();
        formData.append('from_who', '9989015918');
        formData.append('phone', from_who);
        formData.append('body', message);
        formData.append('sent_status', 'true');

        fetch(url, {
            method: "POST",
            headers: ({}),
            body: formData
        }).then(response => {
            if (response.status === 201) {
                console.log(response);
                toaster.notify("Sucessfull message sent", {
                    duration: 2000, type: "success"
                });
                return response.json()
            } else {
                console.log("oh no!", response.status === 404)
            }
        }).then(function (data) {
            console.log('request succeeded with JSON response', data)
        })
    }

    handleChange(e) {
        const {name, value} = e.target;
        this.setState({[name]: value});
    }

    render() {
        const {from_who, to_who, message_status, submitted, message} = this.state;
        return (
            <div className="animated fadeIn">
                <Row>
                    <Col xs="12" md="12">
                        <Card>
                            <CardHeader>
                                <strong>Multi Media Message</strong> Whatsapp
                            </CardHeader>
                            <CardBody>
                                <Form action="" method="post" encType="multipart/form-data" className="form-horizontal">
                                    <FormGroup row>
                                        <Col md="3">
                                            <Label>From </Label>
                                        </Col>
                                        <Col xs="12" md="9">
                                            <p className="form-control-static"><strong>+91-9989015918</strong></p>
                                        </Col>
                                    </FormGroup>
                                    <FormGroup row>
                                        <Col md="3">
                                            <Label htmlFor="file-input">Vcard </Label>
                                        </Col>
                                        <Col xs="12" md="9">
                                            <Input type="file" id="file-input" name="file-input"/>
                                        </Col>
                                    </FormGroup>
                                    <FormGroup row>
                                        <Col md="3">
                                            <Label htmlFor="textarea-input">Message</Label>
                                        </Col>
                                        <Col xs="12" md="9">
                                            <Input type="textarea" name="message" id="textarea-input" rows="9"
                                                   value={message} onChange={this.handleChange}
                                                   placeholder="Message Content..."/>
                                            {submitted && !message &&
                                            <div className="help-block">Text under the file</div>
                                            }
                                        </Col>
                                    </FormGroup>

                                    <FormGroup row>
                                        <Col md="3">
                                            <Label htmlFor="file-multiple-input">Multiple File input</Label>
                                        </Col>
                                        <Col xs="12" md="9">
                                            {/*<Input type="file" id="file-multiple-input" name="file-multiple-input"*/}
                                            {/*       multiple/>*/}
                                            <FilePond allowMultiple={true} maxFiles={5}/>
                                        </Col>
                                    </FormGroup>
                                </Form>
                            </CardBody>
                            <CardFooter>
                                <Button type="submit" size="sm" color="primary" onClick={this.handleSubmit}><i
                                    className="fa fa-dot-circle-o"></i> Submit</Button>
                                <Button type="reset" size="sm" color="danger"><i
                                    className="fa fa-ban"></i> Reset</Button>
                            </CardFooter>
                        </Card>
                    </Col>
                </Row>
            </div>
        );
    }
}

export default MultiMediaMessages;
