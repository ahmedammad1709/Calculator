# Modern Calculator Web App

A beautiful, responsive calculator web application built with Flask backend and modern frontend technologies.

## ✨ Features

- **Modern UI Design**: Glassmorphism design with smooth animations
- **Dark Mode Toggle**: Switch between light and dark themes
- **Responsive Design**: Works perfectly on desktop and mobile devices
- **Full Calculator Functionality**: Addition, subtraction, multiplication, division, percentage
- **Keyboard Support**: Use your keyboard for calculations
- **Interactive Animations**: Button ripple effects and smooth transitions
- **Error Handling**: Graceful error messages for invalid operations
- **Flask Backend**: Optional backend calculation support

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone or download the project files**

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:5000`

## 🎨 Features in Detail

### Calculator Operations
- **Basic Arithmetic**: +, -, ×, ÷
- **Percentage**: Calculate percentages
- **Clear**: Reset calculator (AC)
- **Delete**: Remove last digit (DEL)
- **Decimal Support**: Handle decimal numbers

### UI/UX Features
- **Glassmorphism Design**: Modern glass-like appearance
- **Smooth Animations**: Button hover effects and transitions
- **Ripple Effects**: Material design-inspired button interactions
- **Responsive Layout**: Adapts to different screen sizes
- **Dark/Light Mode**: Toggle between themes with persistent storage

### Keyboard Shortcuts
- **Numbers**: 0-9 keys
- **Operators**: +, -, *, /
- **Enter/=**: Calculate result
- **Backspace**: Delete last digit
- **Escape**: Clear calculator

## 📁 Project Structure

```
Calculator/
├── app.py                 # Flask backend server
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── templates/
│   └── index.html        # Main HTML template
└── static/
    ├── style.css         # Modern CSS styling
    └── script.js         # JavaScript functionality
```

## 🛠️ Technical Details

### Backend (Flask)
- **Route**: `/` - Serves the main calculator page
- **API**: `/calculate` - Handles calculation requests (optional)
- **Security**: Input validation and safe expression evaluation

### Frontend
- **HTML5**: Semantic markup with modern structure
- **CSS3**: Advanced styling with CSS variables and animations
- **JavaScript**: ES6+ class-based calculator logic
- **Font Awesome**: Icons for dark mode toggle
- **Google Fonts**: Inter font family for modern typography

### Responsive Design
- **Mobile First**: Optimized for mobile devices
- **Breakpoints**: 480px and 360px for different screen sizes
- **Flexible Layout**: Grid-based button layout
- **Touch Friendly**: Large touch targets for mobile

## 🎯 Browser Support

- Chrome (recommended)
- Firefox
- Safari
- Edge

## 🔧 Customization

### Colors and Themes
The calculator uses CSS variables for easy theming. Modify the `:root` variables in `style.css` to change colors.

### Adding New Operations
To add new calculator operations:
1. Add the button to `index.html`
2. Add the operation logic in `script.js`
3. Update the display logic if needed

## 📱 Mobile Experience

The calculator is fully optimized for mobile devices:
- Touch-friendly button sizes
- Responsive layout
- Smooth animations
- Proper viewport settings

## 🚀 Deployment

### Local Development
```bash
python app.py
```

### Production Deployment
For production deployment, consider using:
- Gunicorn or uWSGI as WSGI server
- Nginx as reverse proxy
- Environment variables for configuration

## 🤝 Contributing

Feel free to contribute to this project by:
- Reporting bugs
- Suggesting new features
- Submitting pull requests

## 📄 License

This project is open source and available under the MIT License.

---

**Enjoy your modern calculator experience! 🧮✨** 