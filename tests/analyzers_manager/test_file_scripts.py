# This file is a part of IntelOwl https://github.com/intelowlproject/IntelOwl
# See the file 'LICENSE' for copying permission.
from . import _FileAnalyzersScriptsTestCase

# File Analyzer Test Cases


class EXEAnalyzersTestCase(_FileAnalyzersScriptsTestCase):
    @classmethod
    def get_params(cls):
        return {
            **super().get_params(),
            "file_name": "file.exe",
            "file_mimetype": "application/x-dosexec",
            "analyzers_to_execute": [
                "File_Info",
                "PE_Info",
                "ELF_Info",
                "Signature_Info",
                "SpeakEasy",
                "Strings_Info",
                "Qiling_Windows",
                "Qiling_Windows_Shellcode",
                "Qiling_Linux",
                "Qiling_Linux_Shellcode",
                "Intezer_Scan",
                "Cuckoo_Scan",
                "Malpedia_Scan",
                "UnpacMe_EXE_Unpacker",
                "PEframe_Scan",
                "Capa_Info",
                "CapeSandbox",
                "Triage_Scan",
                "Floss",
                "MWDB_Scan",
                "YARAify_File_Scan",
                "Yara",
                "VirusTotal_v2_Get_File",
                "VirusTotal_v2_Scan_File",
                "VirusTotal_v3_Get_File",
                "VirusTotal_v3_Get_File_And_Scan",
                "Cymru_Hash_Registry_Get_File",
                "HybridAnalysis_Get_File",
                "MISPFIRST_Check_Hash",
                "MISP_Check_Hash",
                "MalwareBazaar_Get_File",
                "OTX_Check_Hash",
                "Dragonfly_Emulation",
                "FileScan_Upload_File",
                "Virushee_Upload_File",
                "DocGuard_Upload_File",
            ],
        }


class DLLAnalyzersTestCase(_FileAnalyzersScriptsTestCase):
    @classmethod
    def get_params(cls):
        return {
            **super().get_params(),
            "file_name": "file.dll",
            "file_mimetype": "application/x-dosexec",
            "analyzers_to_execute": ["File_Info", "PE_Info", "SpeakEasy"],
        }


class DocAnalyzersTestCase(_FileAnalyzersScriptsTestCase):
    @classmethod
    def get_params(cls):
        return {
            **super().get_params(),
            "file_name": "document.doc",
            "file_mimetype": "application/msword",
            "analyzers_to_execute": ["Doc_Info"],
        }


class ExcelAnalyzersTestCase(_FileAnalyzersScriptsTestCase):
    @classmethod
    def get_params(cls):
        return {
            **super().get_params(),
            "file_name": "document.xls",
            "file_mimetype": "application/vnd.ms-excel",
            "analyzers_to_execute": ["Xlm_Macro_Deobfuscator"],
        }


class RtfAnalyzersTestCase(_FileAnalyzersScriptsTestCase):
    @classmethod
    def get_params(cls):
        return {
            **super().get_params(),
            "file_name": "document.rtf",
            "file_mimetype": "text/rtf",
            "analyzers_to_execute": ["Rtf_Info"],
        }


class PDFAnalyzersTestCase(_FileAnalyzersScriptsTestCase):
    @classmethod
    def get_params(cls):
        return {
            **super().get_params(),
            "file_name": "document.pdf",
            "file_mimetype": "application/pdf",
            "analyzers_to_execute": ["PDF_Info"],
        }


class HTMLAnalyzersTestCase(_FileAnalyzersScriptsTestCase):
    @classmethod
    def get_params(cls):
        return {
            **super().get_params(),
            "file_name": "page.html",
            "file_mimetype": "text/html",
            "analyzers_to_execute": ["Thug_HTML_Info"],
        }


class JSAnalyzersTestCase(_FileAnalyzersScriptsTestCase):
    @classmethod
    def get_params(cls):
        return {
            **super().get_params(),
            "file_name": "file.jse",
            "file_mimetype": "application/javascript",
            "analyzers_to_execute": ["BoxJS_Scan_JavaScript"],
        }


class APKAnalyzersTestCase(_FileAnalyzersScriptsTestCase):
    @classmethod
    def get_params(cls):
        return {
            **super().get_params(),
            "file_name": "sample.apk",
            "file_mimetype": "application/vnd.android.package-archive",
            "analyzers_to_execute": ["APKiD", "Quark_Engine"],
        }


class PCAPAnalyzersTestCase(_FileAnalyzersScriptsTestCase):
    @classmethod
    def get_params(cls):
        return {
            **super().get_params(),
            "file_name": "example.pcap",
            "file_mimetype": "application/vnd.tcpdump.pcap",
            "analyzers_to_execute": ["Suricata"],
        }


class ELFAnalyzersTestCase(_FileAnalyzersScriptsTestCase):
    @classmethod
    def get_params(cls):
        return {
            **super().get_params(),
            "file_name": "ping.elf",
            "file_mimetype": "application/x-sharedlib",
            "analyzers_to_execute": ["ELF_Info"],
        }


class OneNoteAnalyzersTestCase(_FileAnalyzersScriptsTestCase):
    @classmethod
    def get_params(cls):
        return {
            **super().get_params(),
            "file_name": "sample.one",
            "file_mimetype": "application/onenote",
            "analyzers_to_execute": ["OneNote_Info"],
        }
