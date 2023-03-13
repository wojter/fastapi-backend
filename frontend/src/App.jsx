import './App.css'
import { Box, TableContainer, Table, TableBody, TableRow, TableCell, TextField, Button } from '@mui/material';
import EditIcon from '@mui/icons-material/Edit';
import SendIcon from '@mui/icons-material/Send';
import DeleteIcon from '@mui/icons-material/Delete';
import { useState, useEffect } from 'react';
import axios from 'axios';


function App() {
  const [titles, setTitles] = useState([]);
  const [title, setTitle] = useState({});
  useEffect(() => {
    const response = axios.get('http://127.0.0.1:8000/titles_top')
    console.log(response);
    return setTitles(response.data)
  }, [])
  const fetchTitle = async (id) => {
    const response = await axios.get(`http://127.0.0.1:8000/titles/${id}`)
    return setTitle(response.data)
  }
  const createOrEditTitle = async (id) => {
    if (title.id) {
      await axios.put(`http://127.0.0.1:8000/titles/${id}`, title)
    } else {
      await axios.post(`http://127.0.0.1:8000/titles/`, title)
    }
    await fetchTitles()
    await setTitle({ id: 0, title: '', type: '', description: '', runtime: 0, release_year: 0 })
  }
  const deleteTitle = async (id) => {
    await axios.delete(`http://127.0.0.1:8000/titles/${id}`)
    await fetchTitles()
  }
  return (
    <div>
      <Box m={10}>
        <TableContainer>
          <Table sx={{ minWidth: 650 }} aria-label="simple table">
            <TableBody>
              <TableRow
                sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
              >
                <TableCell>
                  <TextField value={title.title} onChange={(e) => setTitle({ ...title, title: e.target.value })} id="standard-basic" label="Title" variant="standard" />
                </TableCell>

                <TableCell>
                  <TextField value={title.type} onChange={(e) => setTitle({ ...title, type: e.target.value })} id="standard-basic" label="Type" variant="standard" />
                </TableCell>

                <TableCell>
                  <TextField value={title.description} onChange={(e) => setTitle({ ...title, description: e.target.value })} id="standard-basic" label="Description" variant="standard" />
                </TableCell>

                <TableCell>
                  <TextField value={title.release_year} onChange={(e) => setTitle({ ...title, release_year: e.target.value })} id="standard-basic" label="Release Year" variant="standard" />
                </TableCell>

                <TableCell>
                  <TextField value={title.runtime} onChange={(e) => setTitle({ ...title, runtime: e.target.value })} id="standard-basic" label="Runtime" variant="standard" />
                </TableCell>

                <TableCell>
                  <Button onClick={() => createOrEditTitle()} variant="contained" endIcon={<SendIcon />}>
                    Send
                  </Button>
                </TableCell>

              </TableRow>
              <TableRow
                sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
              >
                <TableCell>Title</TableCell>
                <TableCell>Type</TableCell>
                <TableCell>Description</TableCell>
                <TableCell>Release Year</TableCell>
                <TableCell>Runtime</TableCell>
                <TableCell>Edit</TableCell>
                <TableCell>Delete</TableCell>
              </TableRow>
              {titles.map((row) => (
                <TableRow
                  key={row.id}
                  sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                >
                  <TableCell>{row.title}</TableCell>
                  <TableCell>{row.type}</TableCell>
                  <TableCell>{row.description}</TableCell>
                  <TableCell>{row.release_year}</TableCell>
                  <TableCell>{row.runtime}</TableCell>
                  <TableCell>
                    <Button onClick={() => deleteTitle(row.id)} variant="outlined" startIcon={<DeleteIcon />}>
                      Delete
                    </Button>
                  </TableCell>
                  <TableCell>
                    <Button onClick={() => fetchTitle(row.id)} variant="outlined" startIcon={<EditIcon />}>
                      Edit
                    </Button>
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </Box>
    </div>
  )
}

export default App
