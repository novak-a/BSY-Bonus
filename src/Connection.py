#
# Author: Adam Novak
#
# Plagiarism is a sin!
# Plagiarism is a sin!
# Plagiarism is a sin!
#

import dropbox
import sys


class Connection:

    def __init__(self, access_token):
        self.dbx = dropbox.Dropbox(access_token)

    def is_connected(self):
        try:
            return self.dbx.users_get_current_account()
        except Exception as e:
            sys.stderr.write(f"API Error: {e}")
            return None

    def list_files(self, folder_path):
        try:
            result = self.dbx.files_list_folder(folder_path)
            return [entry for entry in result.entries]
        except Exception as e:
            sys.stderr.write(f"Error: {e}")
            return []

    def exist_file(self, file_path):
        try:
            return self.dbx.files_get_metadata(file_path)
        except:
            return None

    def create_file(self, file_path):
        try:
            self.dbx.files_upload("".encode("utf-8"), file_path, mode=dropbox.files.WriteMode("overwrite"))
            return True
        except Exception as e:
            sys.stderr.write(f"Error: {e}")
            return False

    def append_to_file(self, file_path, content):
        try:
            metadata, response = self.dbx.files_download(file_path)
            new_content = response.content + content.encode("utf-8")
            self.dbx.files_upload(new_content, file_path, mode=dropbox.files.WriteMode("overwrite"))
            return True
        except Exception as e:
            sys.stderr.write(f"Error: {e}")
            return False

    def get_file_content(self, file_path):
        try:
            metadata, response = self.dbx.files_download(file_path)
            return response.content
        except Exception as e:
            sys.stderr.write(f"Error: {e}")
            return None

    def delete_file(self, file_path):
        try:
            self.dbx.files_delete_v2(file_path)
            return True
        except Exception as e:
            sys.stderr.write(f"Error: {e}")
            return False
