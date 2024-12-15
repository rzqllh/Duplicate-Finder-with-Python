Duplicate Finder is a Python script to detect similar images within a folder using a combination of **perceptual hashing** and **SIFT feature matching**. This script is designed to help you find duplicate or nearly identical image files based on adjustable tolerance.

---

## 🎯 Key Features

- **Perceptual Hashing**
  - Uses perceptual hashing algorithm to quickly and efficiently detect image similarity.
- **SIFT Feature Matching**
  - Compares image visual features using **Scale-Invariant Feature Transform (SIFT)** for more detailed results.
- **Adjustable Tolerance**
  - Allows customization of similarity levels via hash and SIFT thresholds to meet specific needs.
- **Real-Time Feedback**
  - Provides progress updates during the search so you know which file is being processed.

---

## ⚙️ Requirements

Before running this script, make sure you have installed:

- Python 3.6 or newer
- The following libraries:
  - `opencv-python`
  - `imagehash`
  - `Pillow`

To install the dependencies, use the following command:

```bash
pip install opencv-python imagehash Pillow
```

---

## 🚀 Usage

1. Save the file `Duplicate_finder.py` to your local directory.
2. Run the script using the terminal or command prompt:

```bash
python Duplicate_finder.py
```

3. Enter the path to the source image you want to find duplicates of.
4. Enter the path to the folder where the search will be conducted.
5. The script will search for similar images and display the results in the terminal.

---

## 📝 Example Input and Output

**Input:**

```
Enter the path to the source image: ./example/source.jpg
Enter the path to the folder to search: ./example/folder_to_search
```

**Output:**

```
Calculating hash for the source image...
Starting search for similar images...
Processing file 1/10: ./example/folder_to_search/img1.jpg
...

Similar images found:
./example/folder_to_search/duplicate1.jpg
./example/folder_to_search/duplicate2.jpg
```

---

## ⚡ Adjustable Parameters

You can adjust the following parameters in the `find_duplicates` function:

- `threshold`: Hash difference tolerance (default: 5). The smaller the value, the stricter the search.
- `sift_threshold`: Minimum number of "good matches" for SIFT (default: 10).

---

## 🚧 Limitations

- **Image Quality**
  - This method relies on image quality. Blurry or heavily transformed images may yield less accurate results.
- **Limited File Formats**
  - Supports only common image formats such as PNG, JPEG, BMP, GIF, and TIFF. Non-image files are automatically ignored.
- **Processing Speed**
  - Processing can take time if the number of files is very large, especially when using high SIFT thresholds.

---

## 🤝 Contributions

Welcome to contributions from the community. If you have ideas to improve this script, feel free to:

1. Fork this repository.
2. Make improvements or add features.
3. Submit a pull request.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE). You are free to use and modify this project as needed.

---

## 🎉 Closing

We hope this script proves helpful for your needs. Feel free to share suggestions or feedback!

Happy Coding! 😊
