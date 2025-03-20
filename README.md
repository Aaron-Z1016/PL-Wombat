# Planimation

## Overview

This project utilizes the Planning Domain Definition Language (PDDL) to create animations, bridging the gap between planning algorithms and visual representations. Aimed at researchers and educators in artificial intelligence and computer graphics, it provides an innovative approach to visualize planning solutions. The objective is to enrich the visualization of a broader range of planning domains and to elevate Planimation's usability and functionality. This venture is currently being pursued by six students from COMP90082, employing the Scrum Agile methodology for project management.

## Team Wombat Homepage

https://comp90082-2024-sm1-pl-wombat.atlassian.net/wiki/spaces/2024SM1PLWombat/overview?homepageId=622807

## About this Project

For more information on Planimation and related details, please visit: 

https://nirlipo.github.io/project/planimation/

For more documentation about background information and detailed introduction of this Planimation Project, please visit: 

https://planimation.github.io/documentation/

## Project Demo
We have completed 5 pddl animation problem
1. [Snake](https://editor.planning.domains/#edit_session=KjNbPgVDSJg56Ud)
2. [Ferry](https://editor.planning.domains/#edit_session=nrPNmBSHW7rC2r7)
3. [Driverlog](https://editor.planning.domains/#edit_session=0aq4elpAJjLSwfQ)
4. [Storage](https://editor.planning.domains/#edit_session=5wkcK2cyJtVt23n)
5. [Block-3op](https://editor.planning.domains/#edit_session=EKReIcwS04C5vtE)

We haven't deployed the feautres since we have merge them with team Koala.

Here is a video demonstrating these animated planning problems

https://github.com/COMP90082-2024-SM1/PL-Wombat/assets/110153064/4c1571da-a562-4ee4-a568-70d9956e3bdc

## Getting Started

### Prerequisites

- install Python 3.6
- install Docker

### Installation

1. Clone the Planimation repository:
   ```bash
   git clone https://github.com/COMP90082-2024-SM1/PL-Wombat.git

2. Navigate to the project directory:
   ```bash
   cd PL-Wombat

## Frontend

### Docker Build
1. Under the src folder, build a frontend image in Docker.
   ```bash
   docker build -t planimation/frontend:latest .
2. In container of Docker virtual environment, test the web server is running by visiting localhost:8080 in the browser.
   ```bash
   docker run --name planimation_js_frontend -dp 8080:8080 planimation/frontend:latest

## Backend

### Docker Build
1. Under the src folder
   ```bash
   cd backend-develop/server
2. Build a Backend image in Docker.
   ```bash
   docker build -t planimation/backend:latest .
3. In container of Docker virtual environment, test the web server is running by visiting localhost:8000 in the browser.
   ```bash
   docker run --name some-backend -d -p 8000:8000 planimation/backend:latest

## Animation

### Visualization

Under the AnimationProfiles folder, select a topic folder which contains '.ppdl' file of domain, problem and animation(AP).
Upload these three files to the front-end interface to obtain visualization of the specified problem.

## Tests

### Overview
This directory contains system tests for our project. These tests are designed to verify the functionality and performance of our system under a variety of conditions.

### Structure
The tests are organized as follows:

1. Unit Tests: Tests that cover individual components to ensure they function correctly in isolation.

2. Acceptance Test: Checking whether the application meets the client’s requirements. Acceptance tests are created based on the user stories.

### Running Tests

To run the tests, navigate to the project root and execute the following command:

1. Under the tests folder:
   ```bash
   pytest test_apps.py
2. Under the tests folder:
   ```bash
   pytest test_models.py
3. Under the tests folder:
   ```bash
   pytest test_serializers.py
4. Under the tests folder:
   ```bash
   pytest test_views.py

### Usage
For detailed instructions on how to use Planimation, including setting up animation profiles and executing the visualization tool, refer to the documentation available in the docs directory.

### Documentation
Comprehensive documentation, including architectural overviews, guides on creating animation profiles, and contribution instructions, can be found in the docs folder. The documentation also covers the project's development progress under the Scrum Agile methodology.

### Acknowledgments
Heartfelt thanks to the University of Melbourne and the initial group of students who developed Planimation.
Gratitude is extended to the students from COMP90082 for their dedication to advancing the capabilities of Planimation.
