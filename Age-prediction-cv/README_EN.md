# Age Prediction from Face Images

## Project Description
The retail chain **"Khleb-Sol"** is implementing a computer vision system for processing customer photographs.  
Cameras at checkout areas will help to:

- Analyze customer purchases and recommend products relevant to their age group.
- Control cashier compliance when selling alcohol.

The task was to build a model that predicts the **approximate age of a person from a photo**.

---

## Project Goals
1. Perform exploratory data analysis of the dataset.
2. Prepare the data for training.
3. Build and train a deep neural network.
4. Evaluate and fine-tune the model to improve accuracy.

---

## Technologies Used
- Python 3.7+
- TensorFlow / Keras
- NumPy, Pandas, Matplotlib
- GPU (Tesla V100)

Model: **ResNet / EfficientNet (fine-tuning)**  
Loss function: **MSE / MAE**  
Evaluation metric: **MAE (Mean Absolute Error)**

---

## Results
- Initial training achieved MAE ≈ **12–15**.
- After fine-tuning (ResNet unfreezing and additional training), the model reached **MAE ~7.3** on the validation set.
- This means the average prediction error is about **7 years**, which is acceptable for age estimation tasks.

---

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/age-prediction-cnn.git
   cd age-prediction-cnn
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Train the model:
   ```bash
   python 9_faces_age_efficientnet_tuned.py
   ```

---

## 📌 Conclusion
The model effectively predicts age from facial photographs.  
Its accuracy is sufficient for audience analysis and monitoring cashier compliance in age-restricted product sales.
