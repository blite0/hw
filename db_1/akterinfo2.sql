--
-- PostgreSQL database dump
--

-- Dumped from database version 12.5 (Ubuntu 12.5-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.5 (Ubuntu 12.5-0ubuntu0.20.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: akterinfo; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.akterinfo (
    name character(15),
    email character varying(20),
    age integer,
    movies text
);


ALTER TABLE public.akterinfo OWNER TO postgres;

--
-- Data for Name: akterinfo; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.akterinfo (name, email, age, movies) FROM stdin;
Johnny depp    	johny@gmail.com	57	\N
sergey bezrukov	serge@mail.ru	47	\N
tom hardy      	tomhardy@gmail.com	43	\N
Bruce Willis   	bruce@gmail.com	65	\N
\.


--
-- PostgreSQL database dump complete
--

