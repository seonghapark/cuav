
(cl:in-package :asdf)

(defsystem "radar-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "raw" :depends-on ("_package_raw"))
    (:file "_package_raw" :depends-on ("_package"))
  ))