import os
from flask import Flask, request, render_template, jsonify
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

app = Flask(__name__)

# Initialize Google Drive Authentication
gauth = GoogleAuth()
gauth.LocalWebserverAuth()  # Opens a web browser for OAuth
drive = GoogleDrive(gauth)

@app.route('/')
def index():
    # Get list of files in Google Drive to show in the UI (optional)
    file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    # Convert GoogleDriveFile objects into dictionaries with proper metadata
    files = []
    for file in file_list:
        files.append({
            'id': file['id'],
            'title': file['title'],
            'size': file.get('fileSize', 'Unknown'),
            'link': file['alternateLink']
        })
    return render_template('index.html', files=file_list)

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handles file upload and sends it to Google Drive"""
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files['file']
    file_path = os.path.join("uploads", file.filename)
    file.save(file_path)

    # Upload to Google Drive
    drive_file = drive.CreateFile({'title': file.filename})
    drive_file.SetContentFile(file_path)
    drive_file.Upload()
    
    # Get Shareable Link
    drive_file.InsertPermission({'type': 'anyone', 'role': 'reader'})
    share_url = drive_file['alternateLink']

    os.remove(file_path)  # Clean up local file
    return jsonify({"message": "File uploaded successfully", "share_link": share_url})

@app.route('/delete/<file_id>', methods=['GET'])
def delete_file(file_id):
    """Delete the file from Google Drive"""
    try:
        file = drive.CreateFile({'id': file_id})
        file.Delete()  # Delete the file from Google Drive
        return jsonify({"message": f"File {file_id} deleted successfully."})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
