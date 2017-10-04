from os import listdir
from os.path import isfile, join


class Template:
    """select template, search document using a directory, view existing document, sorting documents which will be sorted alphabetically, open a document. """

    def __init__(self):
        # check if user is logged in.
        # if not user.is_logged_in():
        #     user.log_in()
        pass

    # select template
    # def select_template(self, doc_name):
    #     result = self.search_document(doc_name)
    # doc_name = ['Project Proposal \n Tropic', 'Project Proposal \n
    # Spearmint', 'Meeting notes \n Modern Writer', 'Bronchure \n Geometric',
    # 'Newsletter \n Lively']

    # searching for a document
    def search_document(self, document_name, all_documents):
        if document_name in all_documents:
            return document_name
        else:
            return "No text documents yet. Click the addition button to create a new document."

    # viewing recent documents
    def recent_document(self, num):
        all_the_files = self.read_dir('documents')
        # print(all_the_files)
        files = '\n'.join(all_the_files[:num] if num < len(
            all_the_files) else all_the_files)
        return files

    # sorting out documents
    def sort_document(self, docs):
        if type(docs) is list:
            document = '\n'.join([file for file in sorted(docs)])
            print(document)
        else:
            file_list = docs.split()
            document = '\n'.join([file for file in sorted(file_list)])
            print(document)

        # reading files from a directory
    def read_dir(self, dir_name):
        all_files = [files for files in listdir(
            dir_name) if isfile(join(dir_name, files))]
        return all_files

    # opening documents
    def open_doc(self, doc_name):
        # doc_name = input("Name of the document:")
        documents = open(doc_name, "w")
        for document in all_the_files:
            print(document)


# template = Template()
# print(template.read_dir('documents'))
# print(template.read_dir('templates'))
# print("=" * 20)
# files = template.recent_document(52)
# print(files)
# print("=" * 20)
# template.sort_document(files)
