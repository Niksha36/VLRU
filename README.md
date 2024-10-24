# VLRU Project

This project is a Flask-based API for event data. It includes a recommendation algorithm for sorting events based on their occurrences.

## Setup

### Prerequisites

- Python 3.x
- pip (Python package installer)
- Git
- Git LFS (Large File Storage)

### Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/Niksha36/VLRU.git
   cd VLRU

# Requirements Installation

This document provides instructions for installing the required dependencies for the VLRU project.

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Installation Steps

1. **Install Python 3.x**:
   - Download and install Python from the official website: [Python Downloads](https://www.python.org/downloads/).

2. **Install pip**:
   - Pip is included with Python 3.x. You can verify the installation by running:
     ```sh
     pip --version
     ```

3. **Install the required Python packages**:
   - Navigate to the project directory:
     ```sh
     cd VLRU
     ```
   - Install the dependencies listed in `requirements.txt`:
     ```sh
     pip install -r requirements.txt
     ```

4. **Set up Git LFS (Large File Storage)**:
   - Download and install Git LFS from the official website: [Git LFS](https://git-lfs.github.com/).
   - Initialize Git LFS in your repository:
     ```sh
     git lfs install
     git lfs track "dump.db"
     git add .gitattributes
     git commit -m "Track dump.db with Git LFS"
     ```

By following these steps, you will have all the necessary dependencies installed for the VLRU project.
