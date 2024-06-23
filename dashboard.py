import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# Load model and data
model = joblib.load('model_dropout.joblib')
data = pd.read_csv('prediction_dataset.csv')

# Set page configuration
st.set_page_config(
    page_title="Prediksi Dropout Mahasiswa",
    layout="wide"
)

# Sidebar navigation
st.sidebar.title('Navigasi')
option = st.sidebar.selectbox('Pilih Halaman', ['Dashboard', 'Prediction'])

# Dashboard
if option == 'Dashboard':
    st.title('Dashboard')
    
    st.header('Visualisasi Data Fitur Mahasiswa')

    # Visualisasi data dalam 2 kolom 3 baris
    fig, axes = plt.subplots(2, 2, figsize=(15, 15))

    # Visualisasi 1: Distribusi Usia Saat Pendaftaran
    sns.histplot(data['Age_at_enrollment'], bins=20, ax=axes[0, 0], kde=True)
    axes[0, 0].set_title('Distribusi Usia Saat Pendaftaran')

    # Visualisasi 2: SKS Semester 1 yang Diakui
    sns.histplot(data['Curricular_units_1st_sem_credited'], bins=20, ax=axes[0, 1], kde=True)
    axes[0, 1].set_title('SKS Semester 1 yang Diakui')

    # Visualisasi 3: Evaluasi Semester 1
    sns.histplot(data['Curricular_units_1st_sem_evaluations'], bins=20, ax=axes[1, 0], kde=True)
    axes[1, 0].set_title('Evaluasi Semester 1')

    # Visualisasi 4: SKS Semester 1 yang Lulus
    sns.histplot(data['Curricular_units_1st_sem_approved'], bins=20, ax=axes[1, 1], kde=True)
    axes[1, 1].set_title('SKS Semester 1 yang Lulus')

    st.pyplot(fig)

# Prediction
elif option == 'Prediction':
    st.title('Prediksi Dropout Mahasiswa Jaya Institusi')

    # Background information
    st.header('Latar Belakang')
    st.write("""
    **Jaya Jaya Institut** adalah sebuah institusi pendidikan yang didirikan pada tahun 2000. Institut ini telah menghasilkan banyak lulusan dengan reputasi yang sangat baik. Namun, ada juga banyak mahasiswa yang tidak menyelesaikan pendidikannya atau dikenal dengan sebutan dropout.

    Jumlah dropout yang tinggi merupakan masalah besar bagi setiap institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi mahasiswa yang mungkin akan dropout sedini mungkin sehingga dapat diberikan bimbingan khusus.
    """)

    # How to use
    st.header('Cara Menggunakan')
    st.write("""
    1. Masukkan fitur-fitur mahasiswa pada formulir di bawah.
    2. Model akan memprediksi apakah mahasiswa berisiko untuk dropout.
    3. Prediksi dan probabilitas akan ditampilkan.
    """)

    # Form for user input
    st.header('Masukkan Fitur Mahasiswa')
    def user_input_features():
        col1, col2, col3 = st.columns(3)

        with col1:
            Application_mode = st.selectbox('Mode Aplikasi',
                                            ['Online', 'Kertas', 'Langsung ke Kampus', 'Aplikasi Mobile',
                                             'Agen Pendaftaran', 'Pusat Layanan Pelanggan', 'Telepon',
                                             'Email', 'Surat Pos', 'Pihak Ketiga', 'Event Pendaftaran',
                                             'Kolaborasi dengan Sekolah', 'Sistem Resmi Negara',
                                             'Aplikasi Desktop'], index=0)
            Debtor = st.selectbox('Status Debitur', ['Yes', 'No'], index=0)
            Tuition_fees_up_to_date = st.selectbox('Status Pembayaran SPP', ['Yes', 'No'], index=0)
            Gender = st.selectbox('Jenis Kelamin', ['Male', 'Female'], index=0)
            Scholarship_holder = st.selectbox('Penerima Beasiswa', ['Yes', 'No'], index=0)
            Age_at_enrollment = st.slider('Usia saat Pendaftaran', int(data['Age_at_enrollment'].min()), int(data['Age_at_enrollment'].max()), int(data['Age_at_enrollment'].mean()))

        with col2:
            Curricular_units_1st_sem_credited = st.slider('SKS Semester 1 yang Diakui', int(data['Curricular_units_1st_sem_credited'].min()), int(data['Curricular_units_1st_sem_credited'].max()), int(data['Curricular_units_1st_sem_credited'].mean()))
            Curricular_units_1st_sem_evaluations = st.slider('Evaluasi Semester 1', int(data['Curricular_units_1st_sem_evaluations'].min()), int(data['Curricular_units_1st_sem_evaluations'].max()), int(data['Curricular_units_1st_sem_evaluations'].mean()))
            Curricular_units_1st_sem_approved = st.slider('SKS Semester 1 yang Lulus', int(data['Curricular_units_1st_sem_approved'].min()), int(data['Curricular_units_1st_sem_approved'].max()), int(data['Curricular_units_1st_sem_approved'].mean()))
            Curricular_units_1st_sem_grade = st.slider('Nilai Semester 1', int(data['Curricular_units_1st_sem_grade'].min()), int(data['Curricular_units_1st_sem_grade'].max()), int(data['Curricular_units_1st_sem_grade'].mean()))

        with col3:
            Curricular_units_2nd_sem_enrolled = st.slider('SKS Semester 2 yang Diambil', int(data['Curricular_units_2nd_sem_enrolled'].min()), int(data['Curricular_units_2nd_sem_enrolled'].max()), int(data['Curricular_units_2nd_sem_enrolled'].mean()))
            Curricular_units_2nd_sem_evaluations = st.slider('Evaluasi Semester 2', int(data['Curricular_units_2nd_sem_evaluations'].min()), int(data['Curricular_units_2nd_sem_evaluations'].max()), int(data['Curricular_units_2nd_sem_evaluations'].mean()))
            Curricular_units_2nd_sem_approved = st.slider('SKS Semester 2 yang Lulus', int(data['Curricular_units_2nd_sem_approved'].min()), int(data['Curricular_units_2nd_sem_approved'].max()), int(data['Curricular_units_2nd_sem_approved'].mean()))
            Curricular_units_2nd_sem_grade = st.slider('Nilai Semester 2', int(data['Curricular_units_2nd_sem_grade'].min()), int(data['Curricular_units_2nd_sem_grade'].max()), int(data['Curricular_units_2nd_sem_grade'].mean()))

        mode_mapping = {'Online': 15, 'Kertas': 17, 'Langsung ke Kampus': 1, 'Aplikasi Mobile': 53,
                        'Agen Pendaftaran': 18, 'Pusat Layanan Pelanggan': 44, 'Telepon': 39,
                        'Email': 42, 'Surat Pos': 51, 'Pihak Ketiga': 43, 'Event Pendaftaran': 7,
                        'Kolaborasi dengan Sekolah': 16, 'Sistem Resmi Negara': 5,
                        'Aplikasi Desktop': 10}
        Application_mode = mode_mapping[Application_mode]

        binary_mapping = {'Yes': 1, 'No': 0}
        Debtor = binary_mapping[Debtor]
        Tuition_fees_up_to_date = binary_mapping[Tuition_fees_up_to_date]
        Gender = 1 if Gender == 'Male' else 0
        Scholarship_holder = binary_mapping[Scholarship_holder]

        data_input = {'Application_mode': Application_mode,
                      'Debtor': Debtor,
                      'Tuition_fees_up_to_date': Tuition_fees_up_to_date,
                      'Gender': Gender,
                      'Scholarship_holder': Scholarship_holder,
                      'Age_at_enrollment': Age_at_enrollment,
                      'Curricular_units_1st_sem_credited': Curricular_units_1st_sem_credited,
                      'Curricular_units_1st_sem_evaluations': Curricular_units_1st_sem_evaluations,
                      'Curricular_units_1st_sem_approved': Curricular_units_1st_sem_approved,
                      'Curricular_units_1st_sem_grade': Curricular_units_1st_sem_grade,
                      'Curricular_units_2nd_sem_enrolled': Curricular_units_2nd_sem_enrolled,
                      'Curricular_units_2nd_sem_evaluations': Curricular_units_2nd_sem_evaluations,
                      'Curricular_units_2nd_sem_approved': Curricular_units_2nd_sem_approved,
                      'Curricular_units_2nd_sem_grade': Curricular_units_2nd_sem_grade}
        features = pd.DataFrame(data_input, index=[0])
        return features

    input_df = user_input_features()

    # Combine user input features with the entire dataset
    # This will be useful for encoding the features that are not numerical
    df = pd.concat([input_df, data], axis=0)

    # Preprocess input features
    df = df[:1]  # Select only the first row (the user input data)

    # Make prediction
    prediction = model.predict(df)
    prediction_proba = model.predict_proba(df)

    # Main panel
    st.subheader('Fitur Input Pengguna')
    st.write(input_df)

    st.subheader('Prediksi')
    dropout = 'Ya' if prediction[0] == 1 else 'Tidak'
    st.write(f'Dropout: {dropout}')

    st.subheader('Probabilitas Prediksi')
    st.write(f'Probabilitas dropout: {prediction_proba[0][1]:.2f}')
    st.write(f'Probabilitas tidak dropout: {prediction_proba[0][0]:.2f}')
