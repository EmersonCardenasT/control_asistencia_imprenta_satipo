<?php

    class Errors extends Controller{

        public function index()
        {
            
            $this -> views -> getView($this, 'index');
        }
        
        public function methodo()
        {
            $this -> views -> getView($this, 'error');
        }

        public function permisos()
        {
            $this -> views -> getView($this, 'permisos');
        }

    }

?>