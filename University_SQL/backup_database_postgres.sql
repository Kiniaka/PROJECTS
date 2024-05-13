--
-- PostgreSQL database dump
--

-- Dumped from database version 16.2 (Debian 16.2-1.pgdg120+2)
-- Dumped by pg_dump version 16.3

-- Started on 2024-05-10 19:05:52

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

--
-- TOC entry 4 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: pg_database_owner
--

CREATE SCHEMA public;


ALTER SCHEMA public OWNER TO pg_database_owner;

--
-- TOC entry 3406 (class 0 OID 0)
-- Dependencies: 4
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: pg_database_owner
--

COMMENT ON SCHEMA public IS 'standard public schema';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 224 (class 1259 OID 16614)
-- Name: Grades; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Grades" (
    "Grades_id" integer NOT NULL,
    "Grades" integer,
    "Group_id" integer,
    "Student_id" integer,
    "Subjects_id" integer,
    "Teachers_id" integer,
    "Created_date" timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public."Grades" OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 16613)
-- Name: Grades_Grades_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Grades_Grades_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public."Grades_Grades_id_seq" OWNER TO postgres;

--
-- TOC entry 3407 (class 0 OID 0)
-- Dependencies: 223
-- Name: Grades_Grades_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Grades_Grades_id_seq" OWNED BY public."Grades"."Grades_id";


--
-- TOC entry 218 (class 1259 OID 16544)
-- Name: Groups; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Groups" (
    "Group_id" integer NOT NULL,
    "Group_name" character varying(30) NOT NULL,
    "Created_date" timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public."Groups" OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 16543)
-- Name: Groups_Group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Groups_Group_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public."Groups_Group_id_seq" OWNER TO postgres;

--
-- TOC entry 3408 (class 0 OID 0)
-- Dependencies: 217
-- Name: Groups_Group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Groups_Group_id_seq" OWNED BY public."Groups"."Group_id";


--
-- TOC entry 216 (class 1259 OID 16528)
-- Name: Students; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Students" (
    "Student_id" integer NOT NULL,
    "Student_First_name" character varying(30) NOT NULL,
    "Student_Last_name" character varying(30) NOT NULL,
    "Groups_id" integer,
    "Created_date" timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public."Students" OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 16527)
-- Name: Students_Student_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Students_Student_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public."Students_Student_id_seq" OWNER TO postgres;

--
-- TOC entry 3409 (class 0 OID 0)
-- Dependencies: 215
-- Name: Students_Student_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Students_Student_id_seq" OWNED BY public."Students"."Student_id";


--
-- TOC entry 222 (class 1259 OID 16601)
-- Name: Subjects; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Subjects" (
    "Subjects_id" integer NOT NULL,
    "Subjects_name" character varying(30) NOT NULL,
    "Teachers_id" integer,
    "Created_date" timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public."Subjects" OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 16600)
-- Name: Subjects_Subjects_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Subjects_Subjects_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public."Subjects_Subjects_id_seq" OWNER TO postgres;

--
-- TOC entry 3410 (class 0 OID 0)
-- Dependencies: 221
-- Name: Subjects_Subjects_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Subjects_Subjects_id_seq" OWNED BY public."Subjects"."Subjects_id";


--
-- TOC entry 220 (class 1259 OID 16593)
-- Name: Teachers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Teachers" (
    "Teachers_id" integer NOT NULL,
    "Teacher_First_name" character varying(30) NOT NULL,
    "Teacher_Last_name" character varying(30) NOT NULL,
    "Created_date" timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public."Teachers" OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 16592)
-- Name: Teachers_Teachers_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Teachers_Teachers_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public."Teachers_Teachers_id_seq" OWNER TO postgres;

--
-- TOC entry 3411 (class 0 OID 0)
-- Dependencies: 219
-- Name: Teachers_Teachers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Teachers_Teachers_id_seq" OWNED BY public."Teachers"."Teachers_id";


--
-- TOC entry 3231 (class 2604 OID 16617)
-- Name: Grades Grades_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Grades" ALTER COLUMN "Grades_id" SET DEFAULT nextval('public."Grades_Grades_id_seq"'::regclass);


--
-- TOC entry 3225 (class 2604 OID 16547)
-- Name: Groups Group_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Groups" ALTER COLUMN "Group_id" SET DEFAULT nextval('public."Groups_Group_id_seq"'::regclass);


--
-- TOC entry 3223 (class 2604 OID 16531)
-- Name: Students Student_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Students" ALTER COLUMN "Student_id" SET DEFAULT nextval('public."Students_Student_id_seq"'::regclass);


--
-- TOC entry 3229 (class 2604 OID 16604)
-- Name: Subjects Subjects_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Subjects" ALTER COLUMN "Subjects_id" SET DEFAULT nextval('public."Subjects_Subjects_id_seq"'::regclass);


--
-- TOC entry 3227 (class 2604 OID 16596)
-- Name: Teachers Teachers_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Teachers" ALTER COLUMN "Teachers_id" SET DEFAULT nextval('public."Teachers_Teachers_id_seq"'::regclass);


--
-- TOC entry 3400 (class 0 OID 16614)
-- Dependencies: 224
-- Data for Name: Grades; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Grades" ("Grades_id", "Grades", "Group_id", "Student_id", "Subjects_id", "Teachers_id", "Created_date") FROM stdin;
1	1	1	1	1	1	2024-05-10 08:15:20.258442
6	6	1	2	1	1	2024-05-10 08:15:20.258442
11	2	1	3	1	1	2024-05-10 08:15:20.258442
16	2	1	4	1	1	2024-05-10 08:15:20.258442
21	3	1	5	1	1	2024-05-10 08:15:20.258442
26	5	1	6	1	1	2024-05-10 08:15:20.258442
31	6	1	7	1	1	2024-05-10 08:15:20.258442
36	4	1	8	1	1	2024-05-10 08:15:20.258442
41	2	1	9	1	1	2024-05-10 08:15:20.258442
46	4	1	10	1	1	2024-05-10 08:15:20.258442
51	6	2	11	1	1	2024-05-10 08:15:20.258442
56	1	2	12	1	1	2024-05-10 08:15:20.258442
61	6	2	13	1	1	2024-05-10 08:15:20.258442
66	5	2	14	1	1	2024-05-10 08:15:20.258442
71	5	2	15	1	1	2024-05-10 08:15:20.258442
76	1	2	16	1	1	2024-05-10 08:15:20.258442
81	1	2	17	1	1	2024-05-10 08:15:20.258442
86	3	2	18	1	1	2024-05-10 08:15:20.258442
91	4	2	19	1	1	2024-05-10 08:15:20.258442
96	4	2	20	1	1	2024-05-10 08:15:20.258442
101	5	3	21	1	1	2024-05-10 08:15:20.258442
106	1	3	22	1	1	2024-05-10 08:15:20.258442
111	1	3	23	1	1	2024-05-10 08:15:20.258442
116	3	3	24	1	1	2024-05-10 08:15:20.258442
121	2	3	25	1	1	2024-05-10 08:15:20.258442
126	6	3	26	1	1	2024-05-10 08:15:20.258442
131	3	3	27	1	1	2024-05-10 08:15:20.258442
136	1	3	28	1	1	2024-05-10 08:15:20.258442
141	2	3	29	1	1	2024-05-10 08:15:20.258442
2	5	1	1	2	2	2024-05-10 08:15:20.258442
7	5	1	2	2	2	2024-05-10 08:15:20.258442
12	6	1	3	2	2	2024-05-10 08:15:20.258442
17	3	1	4	2	2	2024-05-10 08:15:20.258442
22	2	1	5	2	2	2024-05-10 08:15:20.258442
27	1	1	6	2	2	2024-05-10 08:15:20.258442
32	4	1	7	2	2	2024-05-10 08:15:20.258442
37	6	1	8	2	2	2024-05-10 08:15:20.258442
42	1	1	9	2	2	2024-05-10 08:15:20.258442
47	4	1	10	2	2	2024-05-10 08:15:20.258442
52	5	2	11	2	2	2024-05-10 08:15:20.258442
57	2	2	12	2	2	2024-05-10 08:15:20.258442
62	3	2	13	2	2	2024-05-10 08:15:20.258442
67	4	2	14	2	2	2024-05-10 08:15:20.258442
72	6	2	15	2	2	2024-05-10 08:15:20.258442
77	1	2	16	2	2	2024-05-10 08:15:20.258442
82	1	2	17	2	2	2024-05-10 08:15:20.258442
87	4	2	18	2	2	2024-05-10 08:15:20.258442
92	6	2	19	2	2	2024-05-10 08:15:20.258442
97	2	2	20	2	2	2024-05-10 08:15:20.258442
102	5	3	21	2	2	2024-05-10 08:15:20.258442
107	3	3	22	2	2	2024-05-10 08:15:20.258442
112	4	3	23	2	2	2024-05-10 08:15:20.258442
117	3	3	24	2	2	2024-05-10 08:15:20.258442
122	5	3	25	2	2	2024-05-10 08:15:20.258442
127	6	3	26	2	2	2024-05-10 08:15:20.258442
132	2	3	27	2	2	2024-05-10 08:15:20.258442
137	1	3	28	2	2	2024-05-10 08:15:20.258442
142	5	3	29	2	2	2024-05-10 08:15:20.258442
3	3	1	1	3	3	2024-05-10 08:15:20.258442
8	3	1	2	3	3	2024-05-10 08:15:20.258442
13	6	1	3	3	3	2024-05-10 08:15:20.258442
18	6	1	4	3	3	2024-05-10 08:15:20.258442
23	3	1	5	3	3	2024-05-10 08:15:20.258442
28	3	1	6	3	3	2024-05-10 08:15:20.258442
33	1	1	7	3	3	2024-05-10 08:15:20.258442
38	4	1	8	3	3	2024-05-10 08:15:20.258442
43	1	1	9	3	3	2024-05-10 08:15:20.258442
48	4	1	10	3	3	2024-05-10 08:15:20.258442
53	5	2	11	3	3	2024-05-10 08:15:20.258442
58	3	2	12	3	3	2024-05-10 08:15:20.258442
63	1	2	13	3	3	2024-05-10 08:15:20.258442
68	5	2	14	3	3	2024-05-10 08:15:20.258442
73	1	2	15	3	3	2024-05-10 08:15:20.258442
78	3	2	16	3	3	2024-05-10 08:15:20.258442
83	5	2	17	3	3	2024-05-10 08:15:20.258442
88	4	2	18	3	3	2024-05-10 08:15:20.258442
93	5	2	19	3	3	2024-05-10 08:15:20.258442
98	3	2	20	3	3	2024-05-10 08:15:20.258442
103	6	3	21	3	3	2024-05-10 08:15:20.258442
108	2	3	22	3	3	2024-05-10 08:15:20.258442
113	2	3	23	3	3	2024-05-10 08:15:20.258442
118	6	3	24	3	3	2024-05-10 08:15:20.258442
123	4	3	25	3	3	2024-05-10 08:15:20.258442
128	2	3	26	3	3	2024-05-10 08:15:20.258442
133	2	3	27	3	3	2024-05-10 08:15:20.258442
138	2	3	28	3	3	2024-05-10 08:15:20.258442
4	2	1	1	4	4	2024-05-10 08:15:20.258442
9	1	1	2	4	4	2024-05-10 08:15:20.258442
14	6	1	3	4	4	2024-05-10 08:15:20.258442
19	5	1	4	4	4	2024-05-10 08:15:20.258442
24	1	1	5	4	4	2024-05-10 08:15:20.258442
29	4	1	6	4	4	2024-05-10 08:15:20.258442
34	1	1	7	4	4	2024-05-10 08:15:20.258442
39	3	1	8	4	4	2024-05-10 08:15:20.258442
44	5	1	9	4	4	2024-05-10 08:15:20.258442
49	2	1	10	4	4	2024-05-10 08:15:20.258442
54	4	2	11	4	4	2024-05-10 08:15:20.258442
59	3	2	12	4	4	2024-05-10 08:15:20.258442
64	3	2	13	4	4	2024-05-10 08:15:20.258442
69	5	2	14	4	4	2024-05-10 08:15:20.258442
74	4	2	15	4	4	2024-05-10 08:15:20.258442
79	4	2	16	4	4	2024-05-10 08:15:20.258442
84	2	2	17	4	4	2024-05-10 08:15:20.258442
89	4	2	18	4	4	2024-05-10 08:15:20.258442
94	1	2	19	4	4	2024-05-10 08:15:20.258442
99	6	2	20	4	4	2024-05-10 08:15:20.258442
104	1	3	21	4	4	2024-05-10 08:15:20.258442
109	5	3	22	4	4	2024-05-10 08:15:20.258442
114	1	3	23	4	4	2024-05-10 08:15:20.258442
119	6	3	24	4	4	2024-05-10 08:15:20.258442
124	6	3	25	4	4	2024-05-10 08:15:20.258442
129	3	3	26	4	4	2024-05-10 08:15:20.258442
134	1	3	27	4	4	2024-05-10 08:15:20.258442
139	2	3	28	4	4	2024-05-10 08:15:20.258442
5	6	1	1	5	5	2024-05-10 08:15:20.258442
10	2	1	2	5	5	2024-05-10 08:15:20.258442
15	3	1	3	5	5	2024-05-10 08:15:20.258442
20	3	1	4	5	5	2024-05-10 08:15:20.258442
25	3	1	5	5	5	2024-05-10 08:15:20.258442
30	4	1	6	5	5	2024-05-10 08:15:20.258442
35	6	1	7	5	5	2024-05-10 08:15:20.258442
40	2	1	8	5	5	2024-05-10 08:15:20.258442
45	6	1	9	5	5	2024-05-10 08:15:20.258442
50	4	1	10	5	5	2024-05-10 08:15:20.258442
55	4	2	11	5	5	2024-05-10 08:15:20.258442
60	6	2	12	5	5	2024-05-10 08:15:20.258442
65	5	2	13	5	5	2024-05-10 08:15:20.258442
70	2	2	14	5	5	2024-05-10 08:15:20.258442
146	2	3	30	1	1	2024-05-10 08:15:20.258442
147	1	3	30	2	2	2024-05-10 08:15:20.258442
143	1	3	29	3	3	2024-05-10 08:15:20.258442
148	5	3	30	3	3	2024-05-10 08:15:20.258442
144	6	3	29	4	4	2024-05-10 08:15:20.258442
149	5	3	30	4	4	2024-05-10 08:15:20.258442
75	1	2	15	5	5	2024-05-10 08:15:20.258442
80	3	2	16	5	5	2024-05-10 08:15:20.258442
85	5	2	17	5	5	2024-05-10 08:15:20.258442
90	1	2	18	5	5	2024-05-10 08:15:20.258442
95	2	2	19	5	5	2024-05-10 08:15:20.258442
100	3	2	20	5	5	2024-05-10 08:15:20.258442
105	5	3	21	5	5	2024-05-10 08:15:20.258442
110	6	3	22	5	5	2024-05-10 08:15:20.258442
115	3	3	23	5	5	2024-05-10 08:15:20.258442
120	5	3	24	5	5	2024-05-10 08:15:20.258442
125	2	3	25	5	5	2024-05-10 08:15:20.258442
130	1	3	26	5	5	2024-05-10 08:15:20.258442
135	3	3	27	5	5	2024-05-10 08:15:20.258442
140	2	3	28	5	5	2024-05-10 08:15:20.258442
145	1	3	29	5	5	2024-05-10 08:15:20.258442
150	3	3	30	5	5	2024-05-10 08:15:20.258442
\.


--
-- TOC entry 3394 (class 0 OID 16544)
-- Dependencies: 218
-- Data for Name: Groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Groups" ("Group_id", "Group_name", "Created_date") FROM stdin;
1	A	2024-05-09 12:14:28.527744
2	B	2024-05-09 12:14:30.221283
3	C	2024-05-09 12:14:33.374317
\.


--
-- TOC entry 3392 (class 0 OID 16528)
-- Dependencies: 216
-- Data for Name: Students; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Students" ("Student_id", "Student_First_name", "Student_Last_name", "Groups_id", "Created_date") FROM stdin;
1	Kazimierz	Wiśniewski	1	2024-05-09 12:16:15.923898
2	Anna	Wójcik	1	2024-05-09 12:16:15.923898
3	Krzystof	Kowalczyk	1	2024-05-09 12:16:15.923898
4	Joanna	Kamińska	1	2024-05-09 12:16:15.923898
5	Katarzyna	Zielińska	1	2024-05-09 12:16:15.923898
6	Zuzanna	Szymanska	1	2024-05-09 12:16:15.923898
7	Julia	Nowak	1	2024-05-09 12:16:15.923898
8	Maja	Wozniak	1	2024-05-09 12:16:15.923898
9	Adam	Dabrowski	1	2024-05-09 12:16:15.923898
10	Maja	Wojciechowska	1	2024-05-09 12:16:15.923898
11	Antoni	Mazur	2	2024-05-09 12:16:15.923898
12	Hanna	Melnyk	2	2024-05-09 12:16:15.923898
13	Jan	Jankowski	2	2024-05-09 12:16:15.923898
14	Lena	Lewandowska	2	2024-05-09 12:16:15.923898
15	Aleksander	Kwiatkowski	2	2024-05-09 12:16:15.923898
16	Oliwia	Kurpis	2	2024-05-09 12:16:15.923898
17	Nikodem	Wojciechowski	2	2024-05-09 12:16:15.923898
18	Wiktoria	Zając	2	2024-05-09 12:16:15.923898
19	Franciszek	Krawczyk	2	2024-05-09 12:16:15.923898
20	Natalia	Król	2	2024-05-09 12:16:15.923898
21	Jakub	Kaczmarek	3	2024-05-09 12:16:15.923898
22	Aleksandra	Majewska	3	2024-05-09 12:16:15.923898
23	Kacper	Piotrowski	3	2024-05-09 12:16:15.923898
24	Laura	Adamczyk	3	2024-05-09 12:16:15.923898
25	Mikołaj	Grabowski	3	2024-05-09 12:16:15.923898
26	Alicja	Dudek	3	2024-05-09 12:16:15.923898
27	Filip	Walczak	3	2024-05-09 12:16:15.923898
28	Zofia	Tomaszewska	3	2024-05-09 12:16:15.923898
29	Wojciech	Szewczyk	3	2024-05-09 12:16:15.923898
30	Agata	Lisowska	3	2024-05-09 12:16:15.923898
\.


--
-- TOC entry 3398 (class 0 OID 16601)
-- Dependencies: 222
-- Data for Name: Subjects; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Subjects" ("Subjects_id", "Subjects_name", "Teachers_id", "Created_date") FROM stdin;
1	English	1	2024-05-10 09:06:29.95744
2	Maths	2	2024-05-10 09:06:36.25462
3	IT	3	2024-05-10 09:06:42.192812
4	Geography	4	2024-05-10 09:06:48.806682
5	Biology	5	2024-05-10 09:06:53.703555
\.


--
-- TOC entry 3396 (class 0 OID 16593)
-- Dependencies: 220
-- Data for Name: Teachers; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Teachers" ("Teachers_id", "Teacher_First_name", "Teacher_Last_name", "Created_date") FROM stdin;
1	James	Jackson	2024-05-10 07:14:44.915744
2	Heidi	Alvarez	2024-05-10 07:16:27.939869
3	Katie	Herman	2024-05-10 07:16:27.955342
4	Robert	Hayes	2024-05-10 07:16:27.960987
5	Aaron	Allen	2024-05-10 07:16:27.966535
\.


--
-- TOC entry 3412 (class 0 OID 0)
-- Dependencies: 223
-- Name: Grades_Grades_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Grades_Grades_id_seq"', 150, true);


--
-- TOC entry 3413 (class 0 OID 0)
-- Dependencies: 217
-- Name: Groups_Group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Groups_Group_id_seq"', 3, true);


--
-- TOC entry 3414 (class 0 OID 0)
-- Dependencies: 215
-- Name: Students_Student_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Students_Student_id_seq"', 1, false);


--
-- TOC entry 3415 (class 0 OID 0)
-- Dependencies: 221
-- Name: Subjects_Subjects_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Subjects_Subjects_id_seq"', 7, true);


--
-- TOC entry 3416 (class 0 OID 0)
-- Dependencies: 219
-- Name: Teachers_Teachers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Teachers_Teachers_id_seq"', 5, true);


--
-- TOC entry 3242 (class 2606 OID 16620)
-- Name: Grades Grades_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Grades"
    ADD CONSTRAINT "Grades_pkey" PRIMARY KEY ("Grades_id");


--
-- TOC entry 3236 (class 2606 OID 16550)
-- Name: Groups Groups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Groups"
    ADD CONSTRAINT "Groups_pkey" PRIMARY KEY ("Group_id");


--
-- TOC entry 3234 (class 2606 OID 16534)
-- Name: Students Students_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Students"
    ADD CONSTRAINT "Students_pkey" PRIMARY KEY ("Student_id");


--
-- TOC entry 3240 (class 2606 OID 16607)
-- Name: Subjects Subjects_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Subjects"
    ADD CONSTRAINT "Subjects_pkey" PRIMARY KEY ("Subjects_id");


--
-- TOC entry 3238 (class 2606 OID 16599)
-- Name: Teachers Teachers_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Teachers"
    ADD CONSTRAINT "Teachers_pkey" PRIMARY KEY ("Teachers_id");


--
-- TOC entry 3244 (class 2606 OID 16636)
-- Name: Grades Grades_Group_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Grades"
    ADD CONSTRAINT "Grades_Group_id_fkey" FOREIGN KEY ("Group_id") REFERENCES public."Groups"("Group_id");


--
-- TOC entry 3245 (class 2606 OID 16621)
-- Name: Grades Grades_Student_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Grades"
    ADD CONSTRAINT "Grades_Student_id_fkey" FOREIGN KEY ("Student_id") REFERENCES public."Students"("Student_id");


--
-- TOC entry 3246 (class 2606 OID 16626)
-- Name: Grades Grades_Subjects_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Grades"
    ADD CONSTRAINT "Grades_Subjects_id_fkey" FOREIGN KEY ("Subjects_id") REFERENCES public."Subjects"("Subjects_id");


--
-- TOC entry 3247 (class 2606 OID 16631)
-- Name: Grades Grades_Teachers_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Grades"
    ADD CONSTRAINT "Grades_Teachers_id_fkey" FOREIGN KEY ("Teachers_id") REFERENCES public."Teachers"("Teachers_id");


--
-- TOC entry 3243 (class 2606 OID 16608)
-- Name: Subjects Subjects_Teachers_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Subjects"
    ADD CONSTRAINT "Subjects_Teachers_id_fkey" FOREIGN KEY ("Teachers_id") REFERENCES public."Teachers"("Teachers_id");


-- Completed on 2024-05-10 19:05:53

--
-- PostgreSQL database dump complete
--

