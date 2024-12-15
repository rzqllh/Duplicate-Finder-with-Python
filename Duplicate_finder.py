import os
import cv2
import imagehash
from PIL import Image
import time
import traceback

def calculate_hash(image_path):
    """Menghitung hash perceptual dari gambar."""
    try:
        image = Image.open(image_path)
        return imagehash.phash(image)
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return None

def sift_feature_match(image_path1, image_path2):
    """Membandingkan dua gambar menggunakan SIFT feature matching OpenCV."""
    try:
        # Load gambar
        img1 = cv2.imread(image_path1, cv2.IMREAD_GRAYSCALE)
        img2 = cv2.imread(image_path2, cv2.IMREAD_GRAYSCALE)

        if img1 is None or img2 is None:
            print(f"Error: Tidak bisa membaca gambar {image_path1} atau {image_path2}")
            return None

        # Inisialisasi SIFT detector
        sift = cv2.SIFT_create()

        # Deteksi keypoints dan deskriptor
        kp1, des1 = sift.detectAndCompute(img1, None)
        kp2, des2 = sift.detectAndCompute(img2, None)

        # Jika deskriptor kosong
        if des1 is None or des2 is None:
            return None

        # FLANN matcher
        index_params = dict(algorithm=1, trees=5)
        search_params = dict(checks=50)
        flann = cv2.FlannBasedMatcher(index_params, search_params)

        matches = flann.knnMatch(des1, des2, k=2)

        # Ratio test untuk filtering matches
        good_matches = []
        for m, n in matches:
            if m.distance < 0.7 * n.distance:
                good_matches.append(m)

        # Return jumlah matches yang bagus
        return len(good_matches)

    except Exception as e:
        print(f"Error saat memproses SIFT: {e}")
        return None

def find_duplicates(source_image_path, folder_path, threshold=5, sift_threshold=10):
    """
    Mencari gambar serupa berdasarkan hash perceptual dan SIFT feature matching.

    Args:
        source_image_path (str): Path ke gambar sumber.
        folder_path (str): Path folder tempat mencari gambar.
        threshold (int): Batas toleransi kesamaan hash (semakin kecil semakin ketat).
        sift_threshold (int): Minimal jumlah good matches untuk SIFT.

    Returns:
        list: Daftar path gambar yang serupa dengan gambar sumber.
    """
    if not os.path.exists(source_image_path):
        raise FileNotFoundError(f"Source image {source_image_path} not found.")

    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"Folder {folder_path} not found.")

    # Hitung hash gambar sumber
    print("Menghitung hash untuk gambar sumber...")
    source_hash = calculate_hash(source_image_path)
    if source_hash is None:
        raise ValueError("Failed to calculate hash for source image.")

    duplicates = []
    total_files = sum([len(files) for _, _, files in os.walk(folder_path)])
    processed_files = 0

    # Iterasi melalui semua file di folder
    print("Memulai pencarian gambar serupa...")
    start_time = time.time()
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)

            # Hanya proses file gambar
            if file.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif', 'tiff')):
                processed_files += 1
                print(f"Memproses file {processed_files}/{total_files}: {file_path}")
                try:
                    # Hitung hash
                    target_hash = calculate_hash(file_path)
                    if target_hash is not None:
                        hash_difference = source_hash - target_hash
                        if hash_difference <= threshold:
                            duplicates.append(file_path)
                            continue  # Skip SIFT jika sudah mirip berdasarkan hash

                    # Jika hash tidak mirip, coba SIFT feature matching
                    sift_matches = sift_feature_match(source_image_path, file_path)
                    if sift_matches is not None and sift_matches >= sift_threshold:
                        duplicates.append(file_path)
                except Exception as e:
                    print(f"Error saat memproses {file_path}: {e}")

    end_time = time.time()
    print(f"Pencarian selesai dalam {end_time - start_time:.2f} detik.")
    return duplicates

# Contoh penggunaan
if __name__ == "__main__":
    source_image = input("Masukkan path gambar sumber: ").strip()
    folder_to_search = input("Masukkan path folder yang akan dicari: ").strip()

    try:
        duplicates = find_duplicates(source_image, folder_to_search)
        if duplicates:
            print("\nGambar serupa ditemukan:")
            for duplicate in duplicates:
                print(duplicate)
        else:
            print("\nTidak ada gambar serupa ditemukan.")
    except Exception as e:
        print("Terjadi kesalahan:\n")
        print(traceback.format_exc())
    finally:
        input("\nPress any key to exit...")
