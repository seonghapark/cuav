
(cl:in-package :asdf)

(defsystem "radar-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "rail" :depends-on ("_package_rail"))
    (:file "_package_rail" :depends-on ("_package"))
    (:file "raw" :depends-on ("_package_raw"))
    (:file "_package_raw" :depends-on ("_package"))
  ))