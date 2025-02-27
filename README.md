# Python QR Code Generator

## **Introduction**
This project is a Python-based QR code generator that helps create customizable QR codes. It uses the `qrcode` module to generate and save QR codes easily.

## **Installation**
To use this project, ensure you have Python installed, then install the required package:

```sh
pip install qrcode[pil]
```

## **Usage**
Create a simple QR code with the following script:

```python
import qrcode

# Create an instance of QRCode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data("Hello, World!")
qr.make(fit=True)

# Generate and save QR code
img = qr.make_image(fill="black", back_color="white")
img.save("qrcode.png")
```

## **Fixing Common Issues**
If you encounter the error:

```
AttributeError: module 'qrcode' has no attribute 'QRCode'
```

### **Solution**
- Rename your script from `qrcode.py` to something else, like `generate_qr.py`.
- Delete the `__pycache__` folder:
  ```sh
  rm -rf __pycache__
  ```
- Run the script again with:
  ```sh
  python generate_qr.py
  ```

## **Best Practices**
✔ Avoid naming scripts after Python libraries.
✔ Use meaningful names for scripts.
✔ Manage dependencies using virtual environments.

## **Contributing**
Feel free to contribute to this project by submitting issues or pull requests.

## **License**
This project is licensed under the MIT License.

## **GitHub Repository**
[Python QR Code Generator](https://github.com/arvindverma63/PythonQrCode.git)

