from back.methods import get_files_list
import json
import jsonpickle
import eel

@eel.expose
def get_files_json(list: list):
	return jsonpickle.encode(list, unpicklable=False)