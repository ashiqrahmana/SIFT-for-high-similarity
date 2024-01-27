import cv2
import os
import numpy as np

# Function to extract SIFT features from an image
def extract_sift_features(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    sift = cv2.SIFT_create()
    keypoints, descriptors = sift.detectAndCompute(image, None)
    return keypoints, descriptors

# Function to match features between the query image and database image
def match_features(query_descriptors, database_descriptors):
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(query_descriptors, database_descriptors, k=2)
    
    # Apply ratio test
    good_matches = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good_matches.append(m)

    return len(good_matches)

# Directory paths for query and database images
query_dir = "E:/task_5/query"
database_dir = "E:/task_5/database"

# List files in the query directory
query_images = [os.path.join(query_dir, file) for file in os.listdir(query_dir) if file.endswith(('.jpg', '.png'))]

# List files in the database directory
database_images = [os.path.join(database_dir, file) for file in os.listdir(database_dir) if file.endswith(('.jpg', '.png'))]

# Results array to store similarity scores
results = []

# Extract features for each query image
for query_image_path in query_images:
    query_keypoints, query_descriptors = extract_sift_features(query_image_path)

    # Compare with each database image
    for database_image_path in database_images:
        database_keypoints, database_descriptors = extract_sift_features(database_image_path)

        # Match features and calculate similarity score
        similarity_score = match_features(query_descriptors, database_descriptors)

        print(query_image_path, database_image_path, similarity_score)

        # Append results to the array
        results.append({
            'query_image': query_image_path,
            'database_image': database_image_path,
            'similarity_score': similarity_score
        })

# Display top 5 results for each query
for query_index, query_image_path in enumerate(query_images):
    print(f"\nTop 5 Results for Query {query_index + 1} - {query_image_path}:")
    
    # Filter results for the current query
    query_results = [result for result in results if result['query_image'] == query_image_path]
    
    # Sort results based on similarity score in descending order
    query_results.sort(key=lambda x: x['similarity_score'], reverse=True)
    
    # Display top 5 results
    for i, result in enumerate(query_results[:5]):
        print(f"{i + 1}. Database Image: {result['database_image']}, Similarity Score: {result['similarity_score']}")
